from pptx import Presentation

def load_template(template_path):
    """Load a PowerPoint template."""
    return Presentation(template_path)

def add_text_to_slide(slide, placeholder_name, text):
    """Add text to a slide using a placeholder name."""
    for shape in slide.shapes:
        if shape.name == placeholder_name:
            shape.text = text
            break

def save_presentation(presentation, output_path):
    """Save the PowerPoint presentation."""
    presentation.save(output_path)
