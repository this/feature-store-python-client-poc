from featurestore import Client

access_token = "..."


def _get_access_token():
    return access_token


if __name__ == '__main__':
    client = Client("demo-api.feature-store.h2o.ai", secure=False, root_certificates=None)
    client.auth.set_obtain_access_token_method(_get_access_token)
    print(client.projects.list())

