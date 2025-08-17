import gradio as gr
from Sorter import Sorter
import os

def sort_files_ui(directory, extensions):
    try:
        sorter = Sorter(directory, extensions.split(','))
        sorted_count, unsorted_count = sorter.sort_files()
        return f"Sorted files: {sorted_count}, Unsorted files: {unsorted_count}"
    except FileNotFoundError as e:
        return str(e)
    except ValueError as e:
        return str(e)


with gr.Blocks(title="File Sorter") as demo:
    gr.Markdown("# File Sorter\nSort files in a given directory by their extensions.")
    with gr.Row():
        directory_input = gr.Textbox(label="Directory", placeholder="Enter the directory path")
        extensions_input = gr.Textbox(label="File Extensions (comma separated)", placeholder="e.g. txt, jpg, pdf")
    sort_button = gr.Button("Sort Files")
    output_text = gr.Textbox(label="Result", interactive=False)

    def on_sort_click(directory, extensions):
        return sort_files_ui(directory, extensions)

    sort_button.click(
        fn=on_sort_click,
        inputs=[directory_input, extensions_input],
        outputs=output_text
    )

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860,share=False, debug=True)
    print("Gradio app is running. Open your browser to http://127.0.0.1:7860 to access it.")