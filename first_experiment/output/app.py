import gradio as gr
import os
from Sorter import Sorter

def sort_files(directory, extensions):
    if not directory or not extensions:
        return "Directory or extensions cannot be empty.", 0, 0
    
    try:
        sorter = Sorter(directory, extensions.split(","))
        sorted_count, unsorted_count = sorter.sort_files()
        return f"Sorted {sorted_count} files.", sorted_count, unsorted_count
    except FileNotFoundError as e:
        return str(e), 0, 0
    except Exception as e:
        return str(e), 0, 0

def reset_changes(directory):
    # Placeholder for reset functionality
    return "Reset functionality not implemented.", 0, 0

with gr.Blocks() as demo:
    gr.Markdown("### File Sorter")
    with gr.Row():
        directory_input = gr.Textbox(label="Directory", placeholder="Enter the directory to sort files...")
        extensions_input = gr.Textbox(label="Extensions (comma-separated)", placeholder="Enter file extensions...")
    
    sort_button = gr.Button("Sort Files")
    reset_button = gr.Button("Reset Changes")
    
    output = gr.Markdown("Output will be displayed here.")
    
    def update_output(directory, extensions):
        msg, sorted_count, unsorted_count = sort_files(directory, extensions)
        output.update(msg)
        return sorted_count, unsorted_count
    
    sort_button.click(fn=update_output, inputs=[directory_input, extensions_input], outputs=output)
    reset_button.click(fn=reset_changes, inputs=directory_input, outputs=output)

demo.launch()