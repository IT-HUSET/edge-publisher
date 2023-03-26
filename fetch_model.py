import time, requests
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from msrest.authentication import ApiKeyCredentials

ENDPOINT = "https://svantescustomvision.cognitiveservices.azure.com/"
training_key = "bbfc90b028f5449ebefe8495f6203460"

credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)

project_id = "0794e238-d77a-4528-97cd-b32abf203fb8"
iteration_id = "b9715c46-8102-4065-85f5-c6d75ce3dee4"
platform = "DockerFile"
flavor = "ARM"

# export = trainer.export_iteration(project_id, iteration_id, platform, flavor, raw=False)
# print("Export initial status is {}".format(export.status)
                                           
#while (export.status != "Done"):
    # print ("Waiting 10 seconds...")
    # time.sleep(10)
export = None
exports = trainer.get_exports(project_id, iteration_id)
print("Found {} exported models".format(len(exports)))
# Locate the export for this iteration and check its status  
for e in exports:
  print("Looking at exported ai-model {}".format(e))
  if e.platform == platform and e.flavor == flavor:
    export = e
    break

if export: 
  print("Export found: ", export)
  # Success, now we can download it
  export_file = requests.get(export.download_uri)
  with open("exported_model.zip", "wb") as file:
    file.write(export_file.content)
else:
  print("Schade, no export found...")
  raise SystemExit(9)
    

