import os
import numpy as np
import pandas as pd

case_dir = "."   # current folder
times = sorted([d for d in os.listdir(case_dir) if d.isdigit()], key=int)

results = []
def read_internal_field(filepath, is_vector=False):
    with open(filepath, "r") as f:
        lines = f.readlines()

    start_idx = None
    for i, line in enumerate(lines):
        if "internalField" in line:
            start_idx = i
            break

    if start_idx is None:
        raise ValueError(f"internalField not found in {filepath}")

    nPoints = int(lines[start_idx+1].strip())   # number of entries

    data_lines = []
    for line in lines[start_idx+2:]:
        line = line.strip()
        if not line:            # skip empty
            continue
        if line.startswith(")") or line.startswith(";"):
            break
        if line.startswith("//"):
            continue
        data_lines.append(line)

    if len(data_lines) < nPoints:
        raise ValueError(f"Expected {nPoints} entries, got {len(data_lines)} in {filepath}")

    if is_vector:
        vals = []
        for line in data_lines:
            if not line.startswith("("):
                continue
            parts = line.strip("()").split()
            vals.append(np.sqrt(sum(float(x)**2 for x in parts)))
        return np.mean(vals)
    else:
        vals = []
        for line in data_lines:
            line = line.strip("()")
            if line:  # skip blanks
                vals.append(float(line))
        return np.mean(vals)

for t in times:
    try:
        U_avg = read_internal_field(os.path.join(case_dir, t, "U"), is_vector=True)
        P_avg = read_internal_field(os.path.join(case_dir, t, "p"))
        Phi_avg = read_internal_field(os.path.join(case_dir, t, "phi"))
        results.append([int(t), U_avg, P_avg, Phi_avg])
        print(f"✅ Processed time {t}")
    except Exception as e:
        print(f"⚠️ Skipping {t}, error: {e}")

if results:
    df = pd.DataFrame(results, columns=["time","U_avg","P_avg","phi_avg"])
    df.to_csv("fields_avg_timeseries.csv", index=False)
    print("🎉 Done: fields_avg_timeseries.csv created with", len(results), "rows.")
else:
    print("❌ No results written. Check parser logic.")

