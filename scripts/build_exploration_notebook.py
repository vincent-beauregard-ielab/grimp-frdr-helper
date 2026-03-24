"""Build and execute the data exploration notebook for rogers_pass_snow_profiles."""

import nbformat as nbf
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
NB_PATH = PROJECT_ROOT / "notebooks" / "rogers_pass_snow_profiles_data_exploration.ipynb"

nb = nbf.v4.new_notebook()
nb.metadata.kernelspec = {
    "display_name": "Python 3",
    "language": "python",
    "name": "python3",
}

cells = []


def md(source: str):
    cells.append(nbf.v4.new_markdown_cell(source.strip()))


def code(source: str):
    cells.append(nbf.v4.new_code_cell(source.strip()))


# ── Title ──────────────────────────────────────────────────────────────
md("""
# Data Exploration: Rogers Pass Snow Profiles

**Dataset:** Snow profile observation datasets, Rogers Pass, Glacier National Park, BC
**Campaign:** March 1-6, 2025
**Sites:** Fidelity, Jim Bay Corner, Hermit, Round Hill, Christiana Ridge
""")

# ── Setup ──────────────────────────────────────────────────────────────
code("""
import pandas as pd
import openpyxl
import os
import json
import struct
import zipfile
import io
from pathlib import Path
from collections import Counter

import warnings
warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

RAW = Path(r"C:/Users/beav3503/dev/grimp_frdr_helper/datasets/rogers_pass_snow_profiles/raw_data/Rogers Pass March 2024-2025")

def summarize_df(df, label=""):
    \"\"\"Print a summary of a DataFrame.\"\"\"
    print(f"--- {label} ---")
    print(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns")
    print(f"Columns: {list(df.columns)}")
    print(f"Dtypes:\\n{df.dtypes.to_string()}")
    print(f"\\nNull counts:\\n{df.isnull().sum().to_string()}")
    # Numeric ranges
    num_cols = df.select_dtypes(include='number').columns
    if len(num_cols) > 0:
        print(f"\\nNumeric ranges:")
        for c in num_cols:
            print(f"  {c}: min={df[c].min()}, max={df[c].max()}, mean={df[c].mean():.4f}")
    # Categorical / object fields
    obj_cols = df.select_dtypes(include='object').columns
    if len(obj_cols) > 0:
        print(f"\\nCategorical value counts (first 10 unique):")
        for c in obj_cols:
            nunique = df[c].nunique()
            vals = df[c].dropna().unique()[:10]
            print(f"  {c}: {nunique} unique — {list(vals)}")
    print()
""")

# ── 1. File inventory ──────────────────────────────────────────────────
md("## 1. File Inventory")

code("""
from collections import defaultdict

file_inventory = defaultdict(list)
total_size = 0

for root, dirs, files in os.walk(RAW):
    for f in files:
        fp = Path(root) / f
        ext = fp.suffix.lower()
        size = fp.stat().st_size
        total_size += size
        rel = fp.relative_to(RAW)
        file_inventory[ext].append((str(rel), size))

print(f"Total files: {sum(len(v) for v in file_inventory.values())}")
print(f"Total size: {total_size / 1e6:.1f} MB")
print()
for ext in sorted(file_inventory.keys()):
    total_ext_size = sum(s for _, s in file_inventory[ext])
    print(f"  {ext:10s}: {len(file_inventory[ext]):4d} files, {total_ext_size/1e6:.2f} MB")
""")

# ── 2. Snow Stratigraphy XLSX ──────────────────────────────────────────
md("""
## 2. Snow Stratigraphy XLSX (StratiTemplate)

One workbook per site-day with snow profile observations (grain type, hardness, density, temperature).
""")

code("""
strati_files = [
    RAW / "Jour 1 - Fidelity" / "Strati_20250301_fidelity.xlsx",
    RAW / "Jour 2 - Jim Bay" / "20250302_JimBay_StratiTemplate.xlsx",
    RAW / "Jour 3 - Hermit" / "20250303_Hermit.xlsx",
    RAW / "Jour 4 - Fidelity" / "20250304_StratiTemplate.xlsx",
    RAW / "Jour 5 - Round Hill" / "20250305_Strati.xlsx",
    RAW / "Jour 6 - RoundHill and Christiana Ridge" / "CRidge_Strati_20250306.xlsx",
    RAW / "Jour 6 - RoundHill and Christiana Ridge" / "Fidelity_Strati_20250306.xlsx",
]

for sf in strati_files:
    print(f"\\n{'='*60}")
    print(f"FILE: {sf.name}")
    print(f"Size: {sf.stat().st_size / 1024:.1f} KB")
    wb = openpyxl.load_workbook(sf, data_only=True, read_only=True)
    print(f"Sheets: {wb.sheetnames}")
    for sname in wb.sheetnames:
        ws = wb[sname]
        rows = list(ws.iter_rows(values_only=True))
        if len(rows) == 0:
            print(f"  Sheet '{sname}': EMPTY")
            continue
        print(f"  Sheet '{sname}': {len(rows)} rows, {len(rows[0]) if rows else 0} cols")
        # Show first 3 rows to understand header structure
        for i, row in enumerate(rows[:5]):
            # Truncate long rows
            display = [str(c)[:30] if c is not None else '' for c in row[:15]]
            print(f"    Row {i}: {display}")
    wb.close()
""")

code("""
# Deep dive into one representative strati file to extract column/variable info
sf = RAW / "Jour 1 - Fidelity" / "Strati_20250301_fidelity.xlsx"
wb = openpyxl.load_workbook(sf, data_only=True, read_only=True)

for sname in wb.sheetnames:
    ws = wb[sname]
    rows = list(ws.iter_rows(values_only=True))
    if len(rows) < 2:
        continue
    print(f"\\n--- Sheet: {sname} ---")
    print(f"Total rows: {len(rows)}")
    # Try to find header row (first non-empty row with string values)
    for i, row in enumerate(rows):
        non_none = [c for c in row if c is not None]
        if len(non_none) > 2 and any(isinstance(c, str) for c in non_none):
            print(f"Likely header at row {i}: {[str(c)[:40] for c in row if c is not None][:20]}")
            break
    # Show all rows up to row 10 for structure
    for i, row in enumerate(rows[:12]):
        vals = [str(c)[:25] if c is not None else 'None' for c in row[:20]]
        print(f"  [{i:2d}] {vals}")
wb.close()
""")

# ── 3. IRIS TXT files ─────────────────────────────────────────────────
md("""
## 3. IRIS TXT Files

IRIS (Infra-Red Integrating Sphere) measures near-infrared reflectance for specific surface area (SSA).
One file per field day. Format: `time, value` pairs.
""")

code("""
iris_files = sorted(RAW.rglob("*.TXT"))
print(f"IRIS files found: {len(iris_files)}")

for irf in iris_files:
    print(f"\\n{'='*60}")
    print(f"FILE: {irf.relative_to(RAW)}")
    print(f"Size: {irf.stat().st_size / 1024:.1f} KB")

    # Try different encodings
    for enc in ['utf-8', 'latin-1', 'cp1252']:
        try:
            text = irf.read_text(encoding=enc)
            break
        except UnicodeDecodeError:
            continue

    lines = text.strip().split('\\n')
    print(f"Total lines: {len(lines)}")
    print(f"First 5 lines:")
    for line in lines[:5]:
        print(f"  {line.rstrip()}")
    print(f"Last 3 lines:")
    for line in lines[-3:]:
        print(f"  {line.rstrip()}")

    # Parse as CSV
    try:
        df = pd.read_csv(irf, header=None, names=['time', 'value'], encoding=enc,
                          skipinitialspace=True)
        print(f"Parsed: {len(df)} rows")
        print(f"  time: dtype={df['time'].dtype}, sample={df['time'].iloc[:3].tolist()}")
        print(f"  value: dtype={df['value'].dtype}, min={df['value'].min()}, max={df['value'].max()}, mean={df['value'].mean():.4f}")
        # Count NaN
        print(f"  NaN count: time={df['time'].isna().sum()}, value={df['value'].isna().sum()}")
    except Exception as e:
        print(f"  Parse error: {e}")
""")

# ── 4. SMP binary .pnt files ──────────────────────────────────────────
md("""
## 4. SMP Binary .pnt Files (SnowMicroPen)

Binary files from the SLF SnowMicroPenetrometer. Read using the `snowmicropyn` library.
""")

code("""
import snowmicropyn

pnt_files = sorted(RAW.rglob("*.pnt"))
print(f"Total .pnt files: {len(pnt_files)}")

# Group by day
from collections import defaultdict
pnt_by_day = defaultdict(list)
for pf in pnt_files:
    day_dir = pf.relative_to(RAW).parts[0]
    pnt_by_day[day_dir].append(pf)

for day, files in sorted(pnt_by_day.items()):
    print(f"  {day}: {len(files)} files")

# Sample one .pnt file in detail
sample_pnt = pnt_files[0]
print(f"\\n--- Sample: {sample_pnt.name} ---")
p = snowmicropyn.Profile.load(str(sample_pnt))
print(f"  Timestamp: {p.timestamp}")
coords = p.coordinates
if coords:
    print(f"  GPS: lat={coords[0]}, lon={coords[1]}")
else:
    print(f"  GPS: None (no valid coordinates in file)")
print(f"  SMP serial: {p.smp_serial}")
print(f"  Overload: {p.overload}")
print(f"  Speed: {p.speed}")

samples = p.samples
print(f"  Samples shape: {samples.shape}")
print(f"  Columns: {list(samples.columns)}")
print(f"  Distance range: {samples['distance'].min():.2f} to {samples['distance'].max():.2f} mm")
print(f"  Force range: {samples['force'].min():.4f} to {samples['force'].max():.4f} N")
print(f"  Force mean: {samples['force'].mean():.4f} N")
print(f"  NaN in force: {samples['force'].isna().sum()}")
""")

code("""
# Summarize all .pnt files: serial numbers, date range, coordinate range
pnt_meta = []
for pf in pnt_files:
    try:
        p = snowmicropyn.Profile.load(str(pf))
        coords = p.coordinates
        pnt_meta.append({
            'file': pf.name,
            'day': pf.relative_to(RAW).parts[0],
            'timestamp': str(p.timestamp),
            'lat': coords[0] if coords else None,
            'lon': coords[1] if coords else None,
            'serial': p.smp_serial,
            'n_samples': len(p.samples),
            'max_depth_mm': p.samples['distance'].max(),
            'max_force_N': p.samples['force'].max(),
        })
    except Exception as e:
        pnt_meta.append({'file': pf.name, 'error': str(e)})

df_pnt = pd.DataFrame(pnt_meta)
print(f"Successfully loaded: {df_pnt['timestamp'].notna().sum()} / {len(df_pnt)}")
if 'error' in df_pnt.columns:
    errors = df_pnt[df_pnt['error'].notna()]
    if len(errors) > 0:
        print(f"Errors: {len(errors)}")
        print(errors[['file', 'error']].to_string())

valid = df_pnt[df_pnt.get('timestamp', pd.Series()).notna()] if 'timestamp' in df_pnt.columns else df_pnt
if len(valid) > 0 and 'lat' in valid.columns:
    print(f"\\nSMP serial numbers: {sorted(valid['serial'].unique())}")
    print(f"Lat range: {valid['lat'].min():.6f} to {valid['lat'].max():.6f}")
    print(f"Lon range: {valid['lon'].min():.6f} to {valid['lon'].max():.6f}")
    print(f"Max depth range: {valid['max_depth_mm'].min():.1f} to {valid['max_depth_mm'].max():.1f} mm")
    print(f"Max force range: {valid['max_force_N'].min():.4f} to {valid['max_force_N'].max():.4f} N")
    print(f"Samples per profile: {int(valid['n_samples'].min())} to {int(valid['n_samples'].max())}")
""")

# ── 5. SMP-derived CSV profiles (SnowScope) ───────────────────────────
md("""
## 5. SMP-Derived CSV Profiles (SnowScope Export)

CSV exports from the SnowScope app. Two formats observed:
- Old format (SN00328): `HH-MM_YYYY_M_D_ProfileNN_SNXXXXX_.csv` with `optical Reflectance Avg` column
- New format (SN00322, SN00304): `YYYY-MM-DD_HHMM_ProfileNN_SNXXXXX.csv`, may lack optical reflectance
""")

code("""
# Find all SnowScope CSV files (in SS_* and SMP directories, plus Jour 6 Christiana)
ss_csv_dirs = [
    RAW / "Jour 1 - Fidelity" / "Spatial_Jimbaycorner" / "SS_SMP_20250301",
    RAW / "Jour 1 - Fidelity" / "Spatial_Jimbaycorner" / "SS_SS1_20250301",
    RAW / "Jour 3 - Hermit" / "Spatial_Hermitt" / "SS_SS2_hermitt_20250303",
    RAW / "Jour 5 - Round Hill" / "Spatial Survey" / "SS_SN322_20250306",
    RAW / "Jour 6 - RoundHill and Christiana Ridge" / "Spatial Survey Christiana Ridge" / "SS4_christridge_20240306",
]

all_ss_csvs = []
for d in ss_csv_dirs:
    if d.exists():
        csvs = sorted(d.glob("*.csv"))
        all_ss_csvs.extend(csvs)
        print(f"{d.relative_to(RAW)}: {len(csvs)} CSV files")

print(f"\\nTotal SnowScope CSVs: {len(all_ss_csvs)}")
""")

code("""
# Parse a sample SnowScope CSV in detail (old format with optical reflectance)
sample_ss = all_ss_csvs[0]
print(f"Sample file: {sample_ss.name}")
print(f"Size: {sample_ss.stat().st_size / 1024:.1f} KB")

text = sample_ss.read_text(encoding='utf-8')
lines = text.strip().split('\\n')
print(f"\\nFull file structure ({len(lines)} lines):")
for i, line in enumerate(lines):
    if i < 20 or i > len(lines) - 4:
        print(f"  [{i:3d}] {line.rstrip()[:100]}")
    elif i == 20:
        print(f"  ... ({len(lines) - 23} data lines omitted) ...")
""")

code("""
# Parse the metadata header and data section of SnowScope CSVs
def parse_snowscope_csv(filepath):
    \"\"\"Parse a SnowScope CSV into metadata dict and data DataFrame.\"\"\"
    text = filepath.read_text(encoding='utf-8')
    lines = text.strip().split('\\n')

    meta = {}
    data_start = None

    for i, line in enumerate(lines):
        if line.startswith('depth (mm)'):
            data_start = i
            break
        if ',' in line:
            parts = line.split(',', 1)
            key = parts[0].strip()
            val = parts[1].strip() if len(parts) > 1 else ''
            if key:
                meta[key] = val

    if data_start is not None:
        # Read data portion
        header_line = lines[data_start]
        cols = [c.strip() for c in header_line.split(',')]
        data_lines = lines[data_start + 1:]
        rows = []
        for dl in data_lines:
            if dl.strip():
                vals = dl.split(',')
                rows.append(vals)
        df = pd.DataFrame(rows, columns=cols)
        # Convert numeric
        for c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce')
        return meta, df
    return meta, pd.DataFrame()

# Parse first file
meta, data = parse_snowscope_csv(all_ss_csvs[0])
print("Metadata keys:", list(meta.keys()))
print("Metadata values:")
for k, v in meta.items():
    print(f"  {k}: {v}")
print(f"\\nData shape: {data.shape}")
print(f"Data columns: {list(data.columns)}")
if len(data) > 0:
    summarize_df(data, "SnowScope data section")
""")

code("""
# Check all SnowScope CSVs for consistency
all_meta_keys = set()
all_data_cols = set()
serial_numbers = set()
locations = []
profile_depths = []
has_optical = 0
no_optical = 0

for csv_f in all_ss_csvs:
    try:
        meta, data = parse_snowscope_csv(csv_f)
        all_meta_keys.update(meta.keys())
        all_data_cols.update(data.columns)
        if 'serialNum' in meta:
            serial_numbers.add(meta['serialNum'])
        if 'Location' in meta and meta['Location'] != 'null':
            parts = meta['Location'].split(',')
            if len(parts) == 2:
                try:
                    locations.append((float(parts[0]), float(parts[1])))
                except ValueError:
                    pass
        if 'profileDepth (mm)' in meta:
            try:
                profile_depths.append(float(meta['profileDepth (mm)']))
            except ValueError:
                pass
        if 'optical Reflectance Avg' in data.columns:
            has_optical += 1
        else:
            no_optical += 1
    except Exception as e:
        print(f"Error parsing {csv_f.name}: {e}")

print(f"All metadata keys: {sorted(all_meta_keys)}")
print(f"All data columns: {sorted(all_data_cols)}")
print(f"Serial numbers: {sorted(serial_numbers)}")
print(f"Files with optical reflectance: {has_optical}")
print(f"Files without optical reflectance: {no_optical}")
if locations:
    lats = [loc[0] for loc in locations]
    lons = [loc[1] for loc in locations]
    print(f"\\nBounding box from SnowScope GPS:")
    print(f"  Lat: {min(lats):.6f} to {max(lats):.6f}")
    print(f"  Lon: {min(lons):.6f} to {max(lons):.6f}")
if profile_depths:
    print(f"Profile depths: {min(profile_depths):.0f} to {max(profile_depths):.0f} mm")
""")

# ── 6. K-band Radar TXT ───────────────────────────────────────────────
md("""
## 6. K-band Radar TXT Files

FMCW radar files with metadata header and I/Q data. One file per measurement point.
""")

code("""
# Find all radar_k txt files
radar_dirs = [
    RAW / "Jour 1 - Fidelity" / "Spatial_Jimbaycorner" / "radar_k",
    RAW / "Jour 2 - Jim Bay" / "Spatial Survey - SMP and Radar K" / "radar_k",
    RAW / "Jour 3 - Hermit" / "Spatial_Hermitt" / "radar_k",
    RAW / "Jour 4 - Fidelity" / "Radar K",
    RAW / "Jour 5 - Round Hill" / "Spatial Survey" / "radar_ka",
]

radar_files = []
for rd in radar_dirs:
    if rd.exists():
        txts = sorted([f for f in rd.glob("*.txt") if not f.name.startswith('.')])
        radar_files.extend(txts)
        print(f"{rd.relative_to(RAW)}: {len(txts)} files")

print(f"\\nTotal radar files: {len(radar_files)}")
""")

code("""
# Parse one radar file in detail
def parse_radar_header(filepath):
    \"\"\"Parse radar K-band TXT file header and return metadata + data.\"\"\"
    text = filepath.read_text(encoding='utf-8')
    lines = text.strip().split('\\n')

    meta = {}
    data_start = None

    for i, line in enumerate(lines):
        line_s = line.strip()
        if line_s.startswith('#') or not line_s:
            continue
        if line_s.startswith('X (m)'):
            data_start = i
            break
        # Parse header key: value pairs
        if ':' in line_s:
            parts = line_s.split(':', 1)
            key = parts[0].strip()
            val = parts[1].strip()
            meta[key] = val

    if data_start is not None:
        header = [c.strip() for c in lines[data_start].split(',')]
        data_rows = []
        for dl in lines[data_start + 1:]:
            dl_s = dl.strip()
            if not dl_s or dl_s.startswith('#') or dl_s.startswith('date'):
                continue
            vals = dl_s.split(',')
            try:
                data_rows.append([float(v.strip()) for v in vals])
            except ValueError:
                continue
        df = pd.DataFrame(data_rows, columns=header)
        return meta, df
    return meta, pd.DataFrame()

sample_radar = radar_files[0]
print(f"Sample: {sample_radar.name}")
meta, data = parse_radar_header(sample_radar)
print(f"\\nHeader metadata:")
for k, v in meta.items():
    print(f"  {k}: {v}")
print(f"\\nData shape: {data.shape}")
print(f"Data columns: {list(data.columns)}")
if len(data) > 0:
    summarize_df(data, "Radar K data")
""")

code("""
# Summarize all radar files: check header consistency
radar_meta_summary = []
for rf in radar_files:
    try:
        meta, data = parse_radar_header(rf)
        radar_meta_summary.append({
            'file': rf.name,
            'day': rf.relative_to(RAW).parts[0],
            'date': meta.get('Date', meta.get('date_record', '')),
            'radar_no': meta.get('Radar No.', ''),
            'start_freq': meta.get('Start-Frequency [MHz]', ''),
            'stop_freq': meta.get('Stop-Frequency [MHz]', ''),
            'n_samples_header': meta.get('Number of Samples', ''),
            'n_data_rows': len(data),
            'n_data_cols': len(data.columns) if len(data) > 0 else 0,
        })
    except Exception as e:
        radar_meta_summary.append({'file': rf.name, 'error': str(e)})

df_radar = pd.DataFrame(radar_meta_summary)
print("Radar file summary:")
print(f"  Total files: {len(df_radar)}")
if 'error' in df_radar.columns:
    errs = df_radar[df_radar['error'].notna()]
    if len(errs) > 0:
        print(f"  Errors: {len(errs)}")
valid_r = df_radar[~df_radar.get('error', pd.Series(dtype=str)).notna()] if 'error' in df_radar.columns else df_radar
if len(valid_r) > 0:
    print(f"  Radar numbers: {sorted(valid_r['radar_no'].unique())}")
    print(f"  Frequency ranges: {sorted(valid_r['start_freq'].unique())} to {sorted(valid_r['stop_freq'].unique())} MHz")
    print(f"  Data rows per file: {valid_r['n_data_rows'].min()} to {valid_r['n_data_rows'].max()}")
    print(f"  Data columns per file: {sorted(valid_r['n_data_cols'].unique())}")
    print(f"  Dates: {sorted(valid_r['date'].unique())}")
""")

# ── 7. Radar/Spatial summary XLSX ──────────────────────────────────────
md("""
## 7. Radar & Spatial Summary XLSX Files

Summary/linkage workbooks that map radar and SMP measurement points to GPS coordinates.
""")

code("""
spatial_xlsx = [
    RAW / "Jour 1 - Fidelity" / "Fidelity Radars and SMP" / "Radar Fidelity point information.xlsx",
    RAW / "Jour 2 - Jim Bay" / "Spatial Survey - SMP and Radar K" / "20250302_JimBayCornerSpatial.xlsx",
    RAW / "Jour 3 - Hermit" / "Spatial_Hermitt" / "20250303_HermitWX_RadarK.xlsx",
    RAW / "Jour 5 - Round Hill" / "Spatial Survey" / "Spatial Survey notes.xlsx",
]

for sf in spatial_xlsx:
    if not sf.exists():
        print(f"MISSING: {sf.name}")
        continue
    print(f"\\n{'='*60}")
    print(f"FILE: {sf.relative_to(RAW)}")
    print(f"Size: {sf.stat().st_size / 1024:.1f} KB")
    wb = openpyxl.load_workbook(sf, data_only=True, read_only=True)
    print(f"Sheets: {wb.sheetnames}")
    for sname in wb.sheetnames:
        ws = wb[sname]
        rows = list(ws.iter_rows(values_only=True))
        if len(rows) == 0:
            print(f"  Sheet '{sname}': EMPTY")
            continue
        print(f"  Sheet '{sname}': {len(rows)} rows")
        for i, row in enumerate(rows[:6]):
            vals = [str(c)[:30] if c is not None else '' for c in row[:15]]
            print(f"    [{i}] {vals}")
    wb.close()
""")

# ── 8. GPS/Spatial CSV files ──────────────────────────────────────────
md("""
## 8. GPS/Spatial CSV and Shapefiles

GPS point files exported from RTK survey equipment.
""")

code("""
gps_csvs = [
    RAW / "Jour 1 - Fidelity" / "Fidelity Radars and SMP" / "Radar Fidelity.csv",
    RAW / "Jour 2 - Jim Bay" / "Spatial Survey - SMP and Radar K" / "jimbaycorner_01032025.csv",
    RAW / "Jour 5 - Round Hill" / "Spatial Survey" / "GPS information" / "ROUND HILL.csv",
]

all_lats = []
all_lons = []
all_elevs = []

for gc in gps_csvs:
    if not gc.exists():
        print(f"MISSING: {gc.name}")
        continue
    print(f"\\n{'='*60}")
    print(f"FILE: {gc.relative_to(RAW)}")
    print(f"Size: {gc.stat().st_size / 1024:.1f} KB")

    df = pd.read_csv(gc)
    summarize_df(df, gc.name)

    # Extract lat/lon for bounding box
    if 'Latitude' in df.columns and 'Longitude' in df.columns:
        lats = df['Latitude'].dropna()
        lons = df['Longitude'].dropna()
        elevs = df['Elevation'].dropna() if 'Elevation' in df.columns else pd.Series()
        all_lats.extend(lats.tolist())
        all_lons.extend(lons.tolist())
        all_elevs.extend(elevs.tolist())
        print(f"  GPS: Lat {lats.min():.6f} to {lats.max():.6f}")
        print(f"       Lon {lons.min():.6f} to {lons.max():.6f}")
        if len(elevs) > 0:
            print(f"       Elev {elevs.min():.1f} to {elevs.max():.1f} m")
""")

code("""
# Examine shapefiles (read zip contents)
shp_zips = [
    RAW / "Jour 1 - Fidelity" / "Fidelity Radars and SMP" / "Radar Fidelity.shp.zip",
    RAW / "Jour 2 - Jim Bay" / "Spatial Survey - SMP and Radar K" / "jimbaycorner_01032025.shp.zip",
    RAW / "Jour 5 - Round Hill" / "Spatial Survey" / "GPS information" / "ROUND HILL.shp.zip",
]

for sz in shp_zips:
    if not sz.exists():
        print(f"MISSING: {sz.name}")
        continue
    print(f"\\n{'='*60}")
    print(f"FILE: {sz.relative_to(RAW)}")
    print(f"Size: {sz.stat().st_size / 1024:.1f} KB")
    with zipfile.ZipFile(sz) as zf:
        print(f"Contents: {zf.namelist()}")
        for name in zf.namelist():
            info = zf.getinfo(name)
            print(f"  {name}: {info.file_size / 1024:.1f} KB")
""")

# ── 9. Bounding box summary ───────────────────────────────────────────
md("## 9. Geographic Bounding Box (from all GPS sources)")

code("""
# Combine bounding box from GPS CSVs and SnowScope locations
from_gps_lats = all_lats.copy()
from_gps_lons = all_lons.copy()

# Add SnowScope locations
if locations:
    for lat, lon in locations:
        from_gps_lats.append(lat)
        from_gps_lons.append(lon)

if from_gps_lats:
    print("Combined bounding box (GPS CSVs + SnowScope):")
    print(f"  North: {max(from_gps_lats):.6f}")
    print(f"  South: {min(from_gps_lats):.6f}")
    print(f"  East:  {max(from_gps_lons):.6f}")
    print(f"  West:  {min(from_gps_lons):.6f}")
    if all_elevs:
        print(f"  Elevation: {min(all_elevs):.1f} to {max(all_elevs):.1f} m")
    print(f"  Total GPS points: {len(from_gps_lats)}")
else:
    print("No GPS data found!")
""")

# ── 10. Morning Hazard Assessment PDFs ─────────────────────────────────
md("""
## 10. Morning Hazard Assessment PDFs

One PDF per day with morning hazard assessment. Structure noted for README, not parsed in detail.
""")

code("""
hazard_pdfs = sorted(RAW.rglob("*Hazard*.pdf"))
print(f"Hazard assessment PDFs: {len(hazard_pdfs)}")
for hp in hazard_pdfs:
    print(f"  {hp.relative_to(RAW)} ({hp.stat().st_size / 1024:.1f} KB)")

# Check structure of one with pypdf
import pypdf
sample_pdf = hazard_pdfs[0]
reader = pypdf.PdfReader(str(sample_pdf))
print(f"\\nSample: {sample_pdf.name}")
print(f"  Pages: {len(reader.pages)}")
page_text = reader.pages[0].extract_text()
if page_text:
    print(f"  First page text (first 500 chars):")
    print(f"  {page_text[:500]}")
""")

# ── 11. Site ReadMe DOCX ──────────────────────────────────────────────
md("""
## 11. Site ReadMe DOCX Files

One per site-day with field notes. Structure noted for README.
""")

code("""
readme_docx = sorted(RAW.rglob("*ReadMe*.docx")) + sorted(RAW.rglob("*readme*.docx"))
# Also check for Read_me pattern
readme_docx += sorted(RAW.rglob("*Read_me*.docx"))
# Deduplicate
readme_docx = sorted(set(readme_docx))

print(f"ReadMe DOCX files: {len(readme_docx)}")
for rd in readme_docx:
    print(f"  {rd.relative_to(RAW)} ({rd.stat().st_size / 1024:.1f} KB)")
""")

# ── 12. Other support files ───────────────────────────────────────────
md("""
## 12. Other / Support Files

Administrative and planning files in the raw data directory.
""")

code("""
other_files = [
    RAW / "AWP",  # Avalanche work permits
    RAW / "Bouffe et infos",
    RAW / "Campagne Roger_s Pass 2025 planification.docx",
    RAW / "Table of content Field Books.docx",
    RAW / "YUL parking reservation.pdf",
    RAW / "StratiTemplate.xlsx",
]

print("Non-scientific support files:")
for of in other_files:
    if of.is_dir():
        files_in = list(of.rglob("*"))
        files_in = [f for f in files_in if f.is_file()]
        print(f"  {of.name}/ ({len(files_in)} files)")
        for f in files_in:
            print(f"    {f.name} ({f.stat().st_size / 1024:.1f} KB)")
    elif of.exists():
        print(f"  {of.name} ({of.stat().st_size / 1024:.1f} KB)")
    else:
        print(f"  {of.name}: NOT FOUND")
""")

# ── 13. Jour 6 anomaly: Two strati files ──────────────────────────────
md("""
## 13. Scope Check: Jour 6 Has Two Stratigraphy Files

Jour 6 contains `CRidge_Strati_20250306.xlsx` (Christiana Ridge) AND `Fidelity_Strati_20250306.xlsx`.
The Fidelity file on Day 6 is unexpected — Day 6 was planned for Round Hill and Christiana Ridge.
""")

code("""
# Check the Jour 6 Fidelity strati file
j6_fidelity = RAW / "Jour 6 - RoundHill and Christiana Ridge" / "Fidelity_Strati_20250306.xlsx"
print(f"FILE: {j6_fidelity.name}")
print(f"Size: {j6_fidelity.stat().st_size / 1024:.1f} KB")
wb = openpyxl.load_workbook(j6_fidelity, data_only=True, read_only=True)
print(f"Sheets: {wb.sheetnames}")
for sname in wb.sheetnames:
    ws = wb[sname]
    rows = list(ws.iter_rows(values_only=True))
    print(f"  Sheet '{sname}': {len(rows)} rows")
    for i, row in enumerate(rows[:5]):
        vals = [str(c)[:30] if c is not None else '' for c in row[:15]]
        print(f"    [{i}] {vals}")
wb.close()
""")

# ── 14. IRIS docx companion file ──────────────────────────────────────
md("## 14. IRIS TXT.docx Companion File")

code("""
# Check the IRIS_20250301.TXT.docx file — likely a companion/readme for the IRIS data
iris_docx = RAW / "Jour 1 - Fidelity" / "IRIS data" / "IRIS_20250301.TXT.docx"
print(f"FILE: {iris_docx.name}")
print(f"Size: {iris_docx.stat().st_size / 1024:.1f} KB")
print("(This appears to be a companion document for the IRIS TXT data format)")
""")

# ── 15. Radar K readme docx ───────────────────────────────────────────
md("## 15. Radar K Readme DOCX (Jour 4)")

code("""
radar_readme = RAW / "Jour 4 - Fidelity" / "Radar K" / "20250304_radar_readme.docx"
if radar_readme.exists():
    print(f"FILE: {radar_readme.name}")
    print(f"Size: {radar_readme.stat().st_size / 1024:.1f} KB")
    print("(Companion document for radar K data from Day 4)")
else:
    print("Not found")
""")

# ── 16. Summary table ─────────────────────────────────────────────────
md("""
## 16. Summary: File Type Inventory

| File Type | Count | Format | Key Variables | Software Required |
|-----------|-------|--------|---------------|-------------------|
| Stratigraphy XLSX | 7 | Multi-sheet Excel | Grain type, hardness, density, temperature by layer | openpyxl, pandas |
| IRIS TXT | 6 | Comma-separated (time, value) | Timestamp, reflectance/SSA value | pandas |
| SMP .pnt | 79 | Binary (SLF format) | Distance (mm), Force (N) | snowmicropyn |
| SnowScope CSV | ~322 | CSV with metadata header | Depth (mm), Hardness (kPa), Optical Reflectance | pandas |
| K-band Radar TXT | ~166 | Text with header + I/Q data | X (m), I1, Q1, I2, Q2 | pandas |
| Spatial Summary XLSX | 4 | Excel workbook | Radar/SMP point linkage, coordinates | openpyxl |
| GPS CSV | 3 | CSV (RTK export) | Lat, Lon, Elevation, Solution status | pandas |
| Shapefiles (.shp.zip) | 3 | Zipped shapefile | Point geometries | geopandas/fiona |
| Hazard Assessment PDF | 6 | PDF | Morning hazard text | pypdf |
| Site ReadMe DOCX | ~8 | Word document | Field notes | python-docx |
| HEIC Photos | 25 | Image | Field notebook pages | (skipped) |
| AWP PDFs | 9 | PDF | Avalanche work permits | (administrative) |
""")

# ── Finalize ───────────────────────────────────────────────────────────
nb.cells = cells
NB_PATH.parent.mkdir(parents=True, exist_ok=True)
nbf.write(nb, str(NB_PATH))
print(f"Notebook written to {NB_PATH}")
