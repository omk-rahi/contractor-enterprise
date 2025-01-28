def breadcrumb_context(request):

    breadcrumbs = []

    if request.path == '/':
        return breadcrumbs

    segments = request.path.strip('/').split('/')

    url = '/'

    for segment in segments:

        url += f"{segment}/"

        new_breadcrumb = {
            "name": segment.replace('_', ' ').replace('-', ' ').title(),
            "url": url,
            "active": request.path == url
        }


        breadcrumbs.append(new_breadcrumb)


    return {"breadcrumbs": breadcrumbs};