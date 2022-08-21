import jinja2

poretrykkdash = jinja2.Template("""
<!DOCTYPE html>
<html lang="en-US">


    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-2.4.3.min.js"></script>
<body>

    <h1>Hello Bokeh!</h1>
    
    <p> Below is a simple plot of stock closing prices </p>
    
    {{ script }}
    
    {{ div }}

</body>

</html>
""")
