import jinja2

poretrykkdash = jinja2.Template("""
<!DOCTYPE html>
<html lang="en-US">

<style>

body {
    background-color: lightblue;
    display:flex;
    align-items:center;
    justify-content:center;
}

#report{
    height: 297mm;
    width: 210mm;
    background-color: white;
    padding: 25mm;
    display:flex;
    set-spacing:10mm;
    flex-direction:column;
}

#title_field{
    height:50mm;
    display:block;
    margin:0;
    padding:0;
}


</style>
<script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-2.4.3.min.js"></script>

<body>
    <div id=report>

        <div id=title_field>
            NGI 
        </div>

        <div id=main_field>
            {{ script }}
            {{ div }}
        </div>

    </div>
</body>




</html>
""")
