"""
Display objects side-by-side in a Jupyter notebook
"""

class Display:
    """
    Display multiple objects side-by-side in a Jupyter notebook

    Class creates HTML representation for each object passed to it. 
    It is useful for comparing multiple Pandas DataFrames or objects that support HTML display.
    """

    # Class HTML template shared between all Display objects/instances
    # {0}: object label
    # {1}: object's HTML representation
    template = """<div style="float: left; padding: 10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
    </div>"""


    def __init__(self, **objects):
        """
        Store named objects to display
        
        Args: 
            **objects: Named objects to display.
            Keyword name is used as label, and value is the object to display.
        """

        # Store passed objects into a dictionary
        # Store as {label: object}
        self.objects = objects


    def _repr_html_(self): # repr_html special method that displays objects as HTML in notebooks
        """
        Return HTML representation of the stored objects.
        
        Returns:
            str: HTML string showing each object side-by-side
        """

        # Build one HTML block per object
        return '\n'.join( # join HTML blocks with \n
            self.template.format(
                name.capitalize(),  # Object label (capitalized)
                getattr(obj, "_repr_html_", lambda: repr(obj))() # Object's HTML representation
            )
            for name, obj in self.objects.items() # Iterate over stored objectss
        )


    def __repr__(self): # fallback text representation, used in non-HTML environments
        """
        Return plain-text representation of the stored objects.
        
        Returns:
            str: Text showing each object's name and regular representation
        """

        # __str__ is conceptually like Java's toString() method override
        # __repr__ is a more "precise" representation of the object compared to __str__
        # Build one plain-text block per object instead of HTML
        return '\n\n'.join(
            name + '\n' + repr(obj)
            for name, obj in self.objects.items()
        )
