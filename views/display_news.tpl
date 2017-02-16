<!-- Navigation -->
<nav class="navbar navbar-default navbar-fixed-top" role="navigation">
	<div class="container">
		<!-- Brand and toggle get grouped for better mobile display -->
		<div class="navbar-header">
			<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
			<span class="sr-only">Toggle navigation</span>
			<span class="icon-bar"></span>
			<span class="icon-bar"></span>
			<span class="icon-bar"></span>
			</button>
			<a class="navbar-brand" href="#">
			<span class="fa-stack fa-lg">
			<i class="fa fa-circle fa-stack-2x text-danger"></i>
			<i class="fa fa-android fa-stack-1x fa-inverse"></i>
			</span>
			</a>
			<div class="divider-vertical"></div>
		</div>
		<!-- Collect the nav links, forms, and other content for toggling -->
		<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
			<!--<ul class="nav navbar-nav">
				<li><a href="/">Today</a></li>
				<li><a href="/all">All</a></li>
				</ul> -->
			<div class="col-sm-3 col-md-3">
				<form class="navbar-form" role="search">
					<input type="text" class="form-control empty" id="iconified" placeholder="&#xF002;"/>
				</form>
			</div>

			<form class="navbar-form pull-right">
				<a class="btn btn-success btn-labeled" href="#" role="button">
				<span class="btn-label"><i class="glyphicon glyphicon-info-sign"></i></span>Site info</a>
			</form>
		</div>
		<!-- /.navbar-collapse -->
	</div>
	<!-- /.container -->
</nav>
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
