<!DOCTYPE html>
<meta name="viewport" content="width=device-width">
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
<link href="//netdna.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">


<script type="text/javascript">
    $('#iconified').on('keyup', function() {
        var input = $(this);
        if(input.val().length === 0) {
            input.addClass('empty');
        } else {
            input.removeClass('empty');
        }
    });
</script>


<style>
    /* modifications for navbar */
    body {
        padding-top: 80px; /* Required padding for .navbar-fixed-top. Remove if using .navbar-static-top. Change if height of navigation changes. */
    }

    .navbar-default {
        background-color: white;
    }

    .navbar-fixed-top {
        min-height: 80px;
    }

        /* modifications for navbar divider */
        .navbar .divider-vertical {
            height: 50px;
            margin: 15px 3px;
            border-right: 1px solid #f2f2f2;
            border-left: 1px solid #ffffff;
        }

        .navbar-inverse .divider-vertical {
            border-right-color: #111111;
            border-left-color: #222222;
        }

        @media (max-width: 767px) {
        .search,
        .navbar-form,
        .navbar-nav > li > a {
            padding-top: 0px;
            padding-bottom: 0px;
            line-height: 80px;
            margin: 0px;
            border:0;
        }

.form-control {
    display: inline-block;
}

        }

        /* modifications for navbar nav links */
        .search,
        .navbar-form,
        .navbar-nav > li > a {
            padding-top: 0px;
            padding-bottom: 0px;
            line-height: 80px;
            margin: 0px;
            border:0;
        }

        /* modifications for navbar form controls */
        .form-control {
            background-color:#f2f2f2;
            outline: none;
            border: none !important;
            -webkit-box-shadow: none !important;
            -moz-box-shadow: none !important;
            box-shadow: none !important;
        }

        /* modifications for navbar search */
        input.empty {
            font-family: FontAwesome;
            font-style: normal;
            font-weight: normal;
            text-decoration: inherit;

        }

        /* modifications for navbar site info button */
        .btn-label { 
            position: relative;
            left: -12px;
            display: inline-block;
            padding: 6px 12px;
            background: rgba(0,0,0,0.15);
            border-radius: 3px 0 0 3px;
        }

        .btn-labeled {
            padding-top: 0;
            padding-bottom: 0;
        }

        .btn { 
            margin-bottom:10px; 
        }

.story {
    margin-top: 50px;
    margin-bottom: 50px;
}

h1,h2,h3,h4,h5,h6 {
margin: 0;
}

.h1,.h2,.h3,.h4,.h5,.h6 {
margin: 0;
}

.h3 {
    margin: 10px 0;
}


.modal-header-about {
    color:#fff;
    padding:9px 15px;
    border-bottom:1px solid #eee;
    background-color: #5cb85c;
    -webkit-border-top-left-radius: 5px;
    -webkit-border-top-right-radius: 5px;
    -moz-border-radius-topleft: 5px;
    -moz-border-radius-topright: 5px;
     border-top-left-radius: 5px;
     border-top-right-radius: 5px;
}




</style>
