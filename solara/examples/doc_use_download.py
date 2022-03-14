from solara.kitchensink import *
from .docutils import *

file_path="yolov3.weights"
url="https://pjreddie.com/media/files/yolov3.weights"
expected_size=248007048

@react.component
def DownloadFile(file_path=file_path, url=url, expected_size=expected_size, on_done=None):
    progress, download_is_done, error, cancel, retry = hooks.use_download(file_path, url, expected_size=expected_size)
    print(url, progress)
    downloaded_size = progress * expected_size
    if on_done:
        on_done(progress==1)
    if download_is_done:
        status = 'Done 🎉'
    else:
        MEGABYTES = 2.0 ** 20.0
        status = "Downloading %s... (%6.2f/%6.2f MB)" % (file_path, downloaded_size / MEGABYTES, expected_size / MEGABYTES)
    # status = "hi"
    # return MarkdownIt(f'{status}')
    with v.Container() as main:
    # with w.VBox() as main:
        with v.Row():
            with v.Col(cols=1):
                progressbar = v.ProgressLinear(value=progress * 100, color='primary', striped=True, height=20)
            # with v.Col(cols=1):
            #     MarkdownIt(f'{status}')
    return main


@react.component
def DocUseDownload():
    with v.Container() as main:
        with w.VBox(layout={'padding': '20px', 'max_width': '1024px'}):
            MarkdownIt('''
# use_download

```python
def use_state(initial: T, key: str = None) -> Tuple[T, Callable[[T], T]]:
    ...
```

use_state can be used to create a variable that is local to this component, and will be preserved during rerenders.

It returns a tuple with the current value, and a setter function that should be called to change the variable. A call to this setter
will trigger a rerender, and will cause the `use_state` function to return the new value on the next render.

## Simple examples

### Click button

Lets start with a Button, that renders how many times it is clicked.
        ''')
            IncludeComponent(DownloadFile, '''
import react_ipywidgets as react
import react_ipywidgets.ipywidgets as w

''', highlight=[6])
#             MarkdownIt("""
# ### Markdown editor
# Lets continue with a more typical pattern, and create new new markdown component
#         """)
#             IncludeComponent(MarkdownIt, md_text="# This is a custom\nMark-*down* **component**")

#             MarkdownIt("""This component does not have state itself, the markdown text can only be set via its argument.
# A common pattern is then to have its parent component manage the state, and pass it down:
# """)
#             # IncludeComponent(MarkdownEditor, md="# Edit me\nand the markdown component **will** *update*", highlight=[3,5,6])
#             MarkdownIt("""Here we see the `MarkdownEditor` component using the `use_state` function to store the markdown text, while letting the `Textarea` component change its value""")
    return main



DownloadFile("yolov3.weights", "https://pjreddie.com/media/files/yolov3.weights", expected_size=248007048)