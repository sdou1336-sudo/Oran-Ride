import json

path="sidox/tasks/generated_patch.json"

with open(path) as f:
    patch=json.load(f)

print("Files to change:")
for item in patch["generated_changes"]:
    print("-", item["type"], item["file"])

answer=input("Approve patch? (yes/no): ")

if answer.lower()=="yes":
    patch["approved"]=True

    with open(path,"w") as f:
        json.dump(patch,f,indent=2)

    print("Patch approved")
else:
    print("Patch rejected")
