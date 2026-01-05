exp_id = input("Experiment ID: ")
contamination_rate = float(input("Contamination Rate: "))

if contamination_rate > 0.10:
    print(f"REJECT: [{exp_id}] has Critical Contamination.")
elif contamination_rate > 0.05:
    print(f"WARNING: [{exp_id}] requires manual review.")
else:
    print("PASS: [ID] is clean.")
    raw = int(input("Raw Reads: "))
    rpm = raw / 1000000
    print(f"Final RPM: [{rpm}]")



