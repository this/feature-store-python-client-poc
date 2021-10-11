from featurestore import Client

access_token = "..."


def _get_access_token():
    return access_token


if __name__ == '__main__':
    root_certificates = "./roots.pem"  # from https://github.com/grpc/grpc/blob/master/etc/roots.pem
    client = Client("demo-api.feature-store.h2o.ai", secure=True, root_certificates=root_certificates)
    client.auth.set_obtain_access_token_method(_get_access_token)
    print(client.projects.list())

