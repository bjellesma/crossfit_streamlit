import os
import streamlit.components.v1 as components

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
_RELEASE = True

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

if not _RELEASE:
    # While we're in development, we can use the hot-reload mechanism in Streamlit
    # to load the component from our frontend/build/ directory
    _component_func = components.declare_component(
        "crossfit_scatter_plot",
        url="http://localhost:3001/crossfit_scatter_plot",
    )
else:
    # When we're distributing the component, we'll build the JSX files to the
    # frontend/build directory.
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("crossfit_scatter_plot", path=build_dir)

def crossfit_scatter_plot(data, layout):
    component_value = _component_func(
        data=data,
        layout=layout
    )
    
    return component_value