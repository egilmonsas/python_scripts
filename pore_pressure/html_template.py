import jinja2

poretrykkdash = jinja2.Template("""
<!DOCTYPE html>
<html lang="en-US">

<style>

body {
    background-color: lightgray;
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

.banner{
    height:40mm;
    display:block;
    margin:0;
    padding:0;
    border-bottom: 1px solid black
}

.title_field{
    height:20mm;
    display:flex;
    flex-direction:row;
    justify-content:space-between;
}

.title_field img{
    height:100%;
}
.title_field h1{
    color:gray;
    bottom:0;
}
.main_field{
    padding-top:10mm;
}

</style>
<script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-2.4.3.min.js"></script>



<body>
    <div id=report>

        <div class=banner>
            <span class=title_field>
                <img src=logo.gif>
                <h1>{{ doc_title }}</h1>
            </span>
        </div>

        <div class=main_field>
            {{ script }}
            {{ div }}
        </div>

    </div>
</body>




</html>
""")
