from chroma import config, adaptors, services
from chroma.ui import presenters, views


# TODO: add logging

def name(output_format=None, view=None, seed: int = None):
    colour_repository = adaptors.get_repository(config.get_datasource_type())
    data = colour_repository.get()

    colour = services.choose_one(data, seed=seed)

    if view is None:
        view = views.build_view(output_format)
    present = presenters.build_presenter(output_format)
    return view(present(colour))

