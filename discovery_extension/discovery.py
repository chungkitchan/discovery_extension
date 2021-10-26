# Extend discovery v2 api for curation
from ibm_watson import DiscoveryV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json,math

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_watson.common import get_sdk_headers

class DiscoveryV2Ext(DiscoveryV2):
    def list_curations(self, project_id: str, **kwargs) -> DetailedResponse:
        """
        (Beta) List curations.
        Lists existing curations for the specified project.
        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListCollectionsResponse` object
        """

        if project_id is None:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_curations')
        headers.update(sdk_headers)

        params = {'version': self.version}

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/curations'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)
        #print(f"request: {request}")
        response = self.send(request, **kwargs)
        return response
    
    def create_curation(self,
                          project_id: str,
                          natural_language_query: str,
                          collection_id: str,
                          document_id: str,
                          **kwargs) -> DetailedResponse:
        """
        (Beta) Add a new curated query.
        Add a new curated query and specify result documents. 
        The curations API methods are beta functionality.
        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str natural_language_query: (optional) A natural language query that
               returns relevant documents by utilizing training data and natural language
               understanding.
        :param str collection_id: The ID of the collection.
        :param str document_id: The ID of the document.
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CollectionDetails` object
        """

        if project_id is None:
            raise ValueError('project_id must be provided')
        if natural_language_query is None:
            raise ValueError('Natural_language_query must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if document_id is None:
            raise ValueError('document_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='create_curation')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {
            'natural_language_query': natural_language_query,
            'curated_results': [{
                'document_id': document_id,
                'collection_id': collection_id
            }]
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/curations'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)
        #print(f"request: {request}")
        response = self.send(request, **kwargs)
        return response
    
    def get_curation(self, project_id: str, curation_id: str,
                       **kwargs) -> DetailedResponse:
        """
        (Beta) Get curation.
        Get details about the specified curation.
        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str curation_id: The ID of the curation.
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CollectionDetails` object
        """

        if project_id is None:
            raise ValueError('project_id must be provided')
        if curation_id is None:
            raise ValueError('curation_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_curation')
        headers.update(sdk_headers)

        params = {'version': self.version}

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'curation_id']
        path_param_values = self.encode_path_vars(project_id, curation_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/curations/{curation_id}'.format(
            **path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)
        #print(f"request: {request}")
        response = self.send(request, **kwargs)
        return response

    def delete_curation(self, project_id: str, curation_id: str,
                          **kwargs) -> DetailedResponse:
        """
        (Beta) Delete a curation.
        Deletes the specified curation from the project. 
        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str curation_id: The ID of the curation.
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if project_id is None:
            raise ValueError('project_id must be provided')
        if curation_id is None:
            raise ValueError('curation_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_collection')
        headers.update(sdk_headers)

        params = {'version': self.version}

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['project_id', 'curation_id']
        path_param_values = self.encode_path_vars(project_id, curation_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/curations/{curation_id}'.format(
            **path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)
        #print(f"request: {request}")
        response = self.send(request, **kwargs)
        return response

    def update_curation(self,
                          project_id: str,
                          curation_id: str,
                          collection_id: str,
                          document_id: str,
                          **kwargs) -> DetailedResponse:
        """
        (Beta) Update a curation.
        Updates the specified collection's name, description, and enrichments.
        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str curation_id: The ID of the curation.
        :param str collection_id: The ID of the collection.
        :param str document_id: The ID of the document.
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CollectionDetails` object
        """

        if project_id is None:
            raise ValueError('project_id must be provided')
        if curation_id is None:
            raise ValueError('collection_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if document_id is None:
            raise ValueError('document_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='update_collection')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {
            'document_id': document_id,
            'collection_id': collection_id
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'curation_id']
        path_param_values = self.encode_path_vars(project_id, curation_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/curations/{curation_id}/curated_results'.format(
            **path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)
        #print(f"request: {request}")
        response = self.send(request, **kwargs)
        return response


# ingest all documents to collection
def ingest_documents(project_id, collection_id, documents, upload_range, discovery_instance, document_type="json", debug=False):
    added = 0
    for d in documents:
        doc = d.copy()
        try: 
            added=added+1
            document_id = doc['document_id']
            content_type = 'application/json'
            filename = doc['extracted_metadata']['filename']
            has_metadata = False
            if 'metadata' in doc:
                metadata = doc['metadata'].copy()
                del doc['metadata']
                has_metadata = True
                

            if debug: print(f"Ingesting document({added}) {filename} with document_id: {document_id}...")
            if has_metadata:
                response = discovery_instance.update_document(project_id= target_project_id,collection_id=target_collection_id,
                                                     file=json.dumps(doc,indent=4),filename = filename,document_id=document_id,
                                                     file_content_type = content_type,metadata = json.dumps(metadata)).get_result()
            else:
                response = discovery_instance.update_document(project_id= target_project_id,collection_id=target_collection_id,
                                                     file=json.dumps(doc,indent=4),filename = filename,document_id=document_id,
                                                     file_content_type = content_type).get_result()
            if debug: 
                print(json.dumps(response, indent=2))
            else:
                if response['status']!="pending":
                      print(json.dumps(response,indent=2))
                if added % 100 ==0:
                      print(f"Ingested {added} documents, with 'pending' status...")
        except Exception as ex:
            print(f"Encounter error while ingesting document({added}) {filename} document_id: {document_id}...")
            print(f"Exception: {ex}")
    print(f"Total {added} documents ingested!!!")

# Download all documents from a collection
def download_all_documents(project_id,collection_id,discovery_instance,query=""):
    count=1000
    results = []
    print(f"Downloading first 1000 results...")  
    response = discovery_instance.query(project_id=project_id,natural_language_query=query,collection_ids=[collection_id],passages=None,count=count).get_result()
    total_documents = response['matching_results']
    print(f"Total matching results: {total_documents}")
    results.extend(response['results'])
    if total_documents >1000:
        for i in range(1, math.ceil(total_documents / 1000)):
            offset = i*1000
            print(f"Downloading offset: {offset} to {offset+1000}...")  
            response = discovery_instance.query(project_id=project_id,natural_language_query=query,collection_ids=[collection_id],
                                       passages=None,count=count,offset=offset).get_result()
            results.extend(response['results'])
    print(f"Total source document downloaded: {len(results)}")
    return results