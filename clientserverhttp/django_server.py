patterns = [
    ("/measurement/store/<int:temperatuur>/<int:neerslag>/", measurement_store),

]

def measurement_store(request, temperatuur, neerslag):
    # sla de meeting op
    m = Measurement(
        neerslag=neerslag,
        temperatuur=temperatuur
    )
    m.save()
    return HttpResponse("Gelukt!")
    