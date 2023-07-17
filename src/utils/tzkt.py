import requests

async def getIndexerStats(rpc) -> list:
    result = []
    url = rpc + '/v1/statistics/current'
    try:
        response : requests.Response = requests.get(url)
        if response.status_code == 200:
            result = response.json()
        else:
            raise Exception(f'getIndexerHead failed with status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        raise Exception('[getIndexerHead] An error occurred:', str(e))
    return result

async def getContractStorage(rpc, address):
    url = rpc + f'/v1/contracts/{address}/storage'
    try:
        response : requests.Response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'getContractStorage failed with status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        raise Exception('[getContractStorage] An error occurred:', str(e))

async def getContractOperationCount(rpc, address):
    url = rpc + f'/v1/operations/transactions/count?anyof.sender.target={address}&status=applied'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'getContractOperationCount failed with status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        raise Exception('[getContractOperationCount] An error occurred:', str(e))

async def getContractOperations(rpc, address, offset = 0):
    url = rpc + f'/v1/operations/transactions?anyof.sender.target={address}&status=applied&limit=100&offset={offset}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'getContractOperations failed with status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        raise Exception('[getContractOperations] An error occurred:', str(e))
