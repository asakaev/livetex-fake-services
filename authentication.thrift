namespace java livetex.auth

typedef string Environment
typedef string Token
typedef string Service
typedef map<string, string> Options

struct ClientEntity {
    1: required string id;
    2: required string type;
    3: optional Options options;
}

struct Endpoint {
    1: required string host;
    2: required i16 port;
    3: optional string protocol;
    4: optional string path;
}

struct AuthenticationResult {
    1: required Token token;
    2: required map<Service, Endpoint> services;
    3: optional Options options;
}

struct CheckTokenResult {
    1: required bool result;
    2: optional Options options;
}

exception InvalidClientError {
    1: required string message;
    2: optional i16 code;
}

service AuthenticationPublic {
    AuthenticationResult getToken(1:ClientEntity client) throws (1:InvalidClientError error);
}

service AuthenticationPrivate {
    void removeToken(1:Token token);
    CheckTokenResult checkToken(1:Token token);

    void addEndpoints(1:Service serv, 2:Environment environment,
        3:list<Endpoint> endpoints);
    void removeEndpoints(1:Service serv, 2:Environment environment,
        3:list<Endpoint> endpoints);
    list<Endpoint> getEndpoints(1:Service serv, 2:Environment environment)

    void changeEnvironment(1:ClientEntity client, 2:Environment environment);
}