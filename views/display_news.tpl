<div class="container">
	<br>
	%for story in news:
	<div class="row notice notice-lg notice-{{story.get_category()}}">
		<div class="col-sm-2">
			<h4>{{story.get_friendly_date()}}</h4>
		</div>
		<div class="col-sm-10">
			<h1>{{story.get_title()}} <span class="label label-danger">Breaking</span></h1>
			<p>{{story.get_story()}} Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
		</div>
		<div class="row nested">
			<div class="col-sm-2 text-uppercase">
				<h4 class="category sport"><span class="glyphicon glyphicon-globe"></span> <strong>{{story.get_category()}}</strong></h4>
			</div>
			<div class="col-sm-10">
				<div class="mobile-social-share btn-group text-uppercase">
					<a data-toggle="dropdown" class="btn btn-success">
					<i class="fa fa-share-alt fa-inverse"></i>
					Share</a>
					<button href="#" data-toggle="dropdown" class="btn btn-success dropdown-toggle share">
					<span class="caret"></span>
					</button>
					<ul class="dropdown-menu">
						<li>
							<a data-original-title="Twitter" rel="tooltip"  href="#" class="btn btn-twitter" data-placement="left">
							<i class="fa fa-twitter"></i>
							</a>
						</li>
						<li>
							<a data-original-title="Facebook" rel="tooltip"  href="#" class="btn btn-facebook" data-placement="left">
							<i class="fa fa-facebook"></i>
							</a>
						</li>
						<li>
							<a data-original-title="Google+" rel="tooltip"  href="#" class="btn btn-google" data-placement="left">
							<i class="fa fa-google-plus"></i>
							</a>
						</li>
						<li>
							<a data-original-title="LinkedIn" rel="tooltip"  href="#" class="btn btn-linkedin" data-placement="left">
							<i class="fa fa-linkedin"></i>
							</a>
						</li>
						<li>
							<a data-original-title="Pinterest" rel="tooltip"  class="btn btn-pinterest" data-placement="left">
							<i class="fa fa-pinterest"></i>
							</a>
						</li>
						<li>
							<a  data-original-title="Email" rel="tooltip" class="btn btn-mail" data-placement="left">
							<i class="fa fa-envelope"></i>
							</a>
						</li>
					</ul>
				</div>
				<div class="btn-group pull-right">
					<button class="btn btn-success btn-circle text-uppercase dropdown-toggle pull-right" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" href="#" id="reply"><span class="glyphicon glyphicon-globe"></span> Sources</button>
					<ul class="dropdown-menu">
						%for source in story.get_sources():
						<li><a href="{{source.url}}">{{source.name}}</a></li>
						%end
					</ul>
				</div>
			</div>
		</div>
	</div>
	%end
</div>
<script>
	$(document).ready(function(){
	    $(".dropdown-toggle").dropdown();
	});
</script>