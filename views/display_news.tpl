<nav class="navbar navbar-inverse navbar-fixed-top">
  <div class="container">


    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed left" data-toggle="collapse" data-target="#menu">
        <span class="sr-only">RN</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="#"><strong>Real News</strong></a>
    </div>


    <div class="collapse navbar-collapse" id="menu">
      <ul class="nav navbar-nav">
        <li class="active"><a href="#">Stories</a></li>
        <li><a href="#info" data-toggle="modal">About</a></li>
      </ul> 
    </div><!-- /.navbar-collapse #menu -->


  </div><!-- /.container -->
</nav>



<nav class="navbar navbar-default navbar-fixed-top subnav">
  <div class="container">


    <div class="collapse navbar-collapse pull-left">
      <ul class="nav navbar-nav">
        <li><a href="/">Today</a></li>
        <li><a href="/all">All</a></li>
      </ul>
    </div><!-- /.navbar-collapse #menu -->



    <form class="hidden-lg hidden-md hidden-sm">
        <div class="form-group">
          <select id="subnavdrop" class="form-control" onchange="location = this.value;">
            <option value="/#">Today</option>
            <option value="/all">All</option>
          </select>
        </div>
    </form>



  </div><!-- /.container -->
</nav>



 <!-- Modal -->
    <div class="modal fade" id="info" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header modal-header-about">
                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
                    <h1><i class="glyphicon glyphicon-info-sign"></i> About</h1>
                </div>
                <div class="modal-body">
					<p>Provide news that is important, impartial and accurate in an easy to digest format.</p>					
                    <p>The Real News Bot works like this</p>
                    <ul>
                    <li>1. Scour the internet for news stories from multiple, reliable sources</li>
                    <li>2. Extract only verified facts and remove opinions <span class="label label-danger">Coming soon</span></li>
                    <li>3. Sumarize the story</li>
                    <li>4. Calculate importance of story based <span class="label label-danger">Coming soon</span></li>
                    <li>5. Categorise and tag story <span class="label label-danger">Coming soon</span></li>
                    </ul>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-default pull-left" data-dismiss="modal">Close</button>
                </div>
            </div><!-- /.modal-content -->
        </div><!-- /.modal-dialog -->
    </div><!-- /.modal -->



<!-- Page Content -->
<div class="container">
	%for story in news:
	<div class="row story">
		<div class="time col-xs-12">
			<h4 class="h4"><small>{{story.get_friendly_date()}}</small></h4>
		</div>
		<div class="headline col-xs-12">
			<h2 class="h3">{{story.get_title()}}</h2>
		</div>

		<div class="story-text col-xs-12">
			<div class="well"><p>{{story.get_story()}}</p></div>
		</div>

		<div class="metadata col-xs-12">
			%if story.is_breaking() is True: 
			<button class="btn btn-danger btn-xs" type="button"><strong>BREAKING</strong></button>
			%end
			<!-- <button class="btn btn-info btn-xs" type="button"><strong>Politics</strong></button>-->
			<div class="btn-group btn-group-success ">
				<button class="btn btn-success btn-xs" type="button"><strong>Sources</strong></button>
				<button data-toggle="dropdown" class="btn btn-success btn-xs dropdown-toggle" type="button"><span class="caret"></span>
				</button>
				<ul class="dropdown-menu">
					%for source in story.get_sources():
					<li><a href="{{source.url}}">{{source.name}}</a></li>
					%end
				</ul>
			</div>
		</div>
	</div>
	%end
</div>
<script>
	$(document).ready(function(){
	    $(".dropdown-toggle").dropdown();
	});
	
	// Sets active link in Bootstrap menu
	// Add this code in a central place used\shared by all pages
	// like your _Layout.cshtml in ASP.NET MVC for example
	$('a[href="' + this.location.pathname + '"]').parents('li,ul').addClass('active');

    // This is for the subnav drop down to ensure it always shows the page we are on
    $("#subnavdrop option[value='" + location.pathname + "']").prop('selected', true);

</script>
