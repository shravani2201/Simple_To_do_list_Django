package example.authz

default allow = false

allow {
    input.user == "admin"
    input.action == "add"
}

allow {
    input.user == "admin"
    input.action == "delete"
}

allow {
    input.user == "guest"
    input.action == "add"
}
