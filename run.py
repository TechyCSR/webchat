from server.app     import app
from server.website import Website
from server.backend import Backend_Api




if __name__ == '__main__':
    site_config = 2000
    
    site = Website(app)
    for route in site.routes:
        app.add_url_rule(
            route,
            view_func = site.routes[route]['function'],
            methods   = site.routes[route]['methods'],
        )

    backend_api  = Backend_Api(app)
    for route in backend_api.routes:
        app.add_url_rule(
            route,
            view_func = backend_api.routes[route]['function'],
            methods   = backend_api.routes[route]['methods'],
        )

    print(f"Running on port 2000")
    app.run(**site_config)
    print(f"Closing port 2000")






