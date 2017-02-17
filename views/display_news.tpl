<!-- Navigation -->
<nav class="navbar navbar-default navbar-fixed-top" role="navigation">
	<div class="container">

		<!-- Brand and toggle get grouped for better mobile display -->
		<div class="navbar-header pull-left">
			<a class="navbar-brand" href="#">
			<span class="fa-stack fa-lg">
			<i class="fa fa-circle fa-stack-2x text-danger"></i>
			<i class="fa fa-android fa-stack-1x fa-inverse"></i>
			</span>
			</a>
			<div class="divider-vertical"></div>
		</div>


        <!-- 'Sticky' (non-collapsing) left-side menu item(s) -->
        <div class="collapse navbar-collapse navbar-header pull-left">

				<form class="navbar-form" role="search">
					<input type="text" class="form-control empty" id="iconified" placeholder="&#xF002;"/>
				</form>
		</div>

        <!-- 'Sticky' (non-collapsing) right-side menu item(s) -->
        <div class="collapse navbar-collapse navbar-header pull-right">

			<form class="navbar-form pull-left">
				<a class="btn btn-success btn-labeled" href="#success" role="button" data-toggle="modal">
					<span class="btn-label"><i class="glyphicon glyphicon-info-sign"></i></span>Site info
				</a>
			</form>
        

		 <!-- Required bootstrap placeholder for the collapsed menu -->
		<!--	<button type="button" class="navbar-toggle pull-right" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
			<span class="sr-only">Toggle navigation</span>
			<span class="icon-bar"></span>
			<span class="icon-bar"></span>
			<span class="icon-bar"></span>
			</button>-->

		</div>



		<!-- Collect the nav links, forms, and other content for toggling -->
		<div class="collapse navbar-collapse navbar-left">
			<!--<ul class="nav navbar-nav navbar-right">
				<li><a href="/">Today</a></li>
				<li><a href="/all">All</a></li>
				</ul> -->




		</div>
		<!-- /.navbar-collapse -->


	</div>
	<!-- /.container -->
</nav>


 <!-- Modal -->
    <div class="modal fade" id="success" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header modal-header-about">
                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
                    <h1><i class="glyphicon glyphicon-info-sign"></i> Site info</h1>
                </div>
                <div class="modal-body">
					<h2>Purpose</h2>
					<p>Provide news that is important, impartial and accurate in an easy to digest format.</p>
					<h2>How does the Real News Bot work</h2>					
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
			<!-- <p>{{story.get_story()}}</p>-->
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
</script>
