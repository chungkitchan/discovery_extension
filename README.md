# Discovery python SDK extension for curation

## 1. List curations
<code>
curations = discovery.list_curations(project_id=f'{project_id}').get_result()
print(json.dumps(curations,indent=2))
</code>

## 2. Get curation details
<code>
curation_details = discovery.get_curation( project_id,curation_id).get_result()
print(json.dumps(curation_details,indent=2))
</code>

## 3. Create curation
<code>
response = discovery.create_curation(project_id=f'{project_id}',natural_language_query="query text",collection_id=f'{collection_id}',document_id=f'{document_id}').get_result()
print(json.dumps(response,indent=2))
</code>

## 4. Delete curation
<code>
response = discovery.delete_curation(project_id=f'{project_id}',curation_id=f'{curation_id}').get_result()
print(json.dumps(response,indent=2))
</code>

## 4. Update curation
<code>
response = discovery.update_curation(project_id=f'{project_id}',curation_id=f'{curation_id}',collection_id=f'{collection_id}',document_id=f'{document_id}').get_result()
print(json.dumps(response,indent=2))
</code>
