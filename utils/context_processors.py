def breadcrumb_context(request):

    breadcrumbs = []

    segments = request.path.strip('/').split('/')

    url = ''

    for segment in segments:

        url += f"{segment}/"

        new_breadcrumb = {
            "name": segment.replace('_', ' ').title(),
            "url": url,
            "active": request.path.strip('/') == url.strip('/')
        }


        breadcrumbs.append(new_breadcrumb)

    print(breadcrumbs)

    return {"breadcrumbs": breadcrumbs};