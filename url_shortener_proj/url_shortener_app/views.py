from django.shortcuts import render, redirect
import uuid
#if this used a database I would not be using function based views, instead of class based news
urls_dict = {}

def index(request):
    if request.method == "POST":
        #get original url from form
        original_url = request.POST.get("original_url")
        identifier = None
        while True:
            #used hex to not have - in the url and restricted to 6 characters, also validates it is not a key already in the dictionary
            identifier = uuid.uuid4().hex[:6]
            if identifier not in urls_dict:
                break
        #add url to dictionary
        urls_dict[identifier] = original_url

        #send shortened url to view
        shortened_url = request.build_absolute_uri(f"/{identifier}")
        return render(request, "index.html", {"shortened_url": shortened_url})

    return render(request, "index.html")


def redirect_to_original_url(request, identifier):
    #retrieve original URL from in-memory dictionary
    original_url = urls_dict.get(identifier)

    if original_url:
        #redirect to the original URL
        return redirect(original_url)
    else:
        return render(request, "not_found.html")
