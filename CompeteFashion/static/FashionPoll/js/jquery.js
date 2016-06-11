$(document).ready(function(){
$('#like').click(function(){
	var pid, liked, unliked,x,y;
	pid = $(this).attr("fashionistaId");
	liked = $(this).attr("userId");
	unliked = $('#like2').attr("userId");
	$.get('/FashionPoll/like-picture/', { pic_id1 : pid, liked : liked, unliked : unliked  }, function(data){
		if(!data.hasOwnProperty('available'))
		{
			x = "http://127.0.0.1:8000/media/"+data[0].fields.fashionista_picture;
			y = "http://127.0.0.1:8000/media/"+data[1].fields.fashionista_picture;
			$('#name1').html(data[0].fields.user);
			$('#name2').html(data[1].fields.user);
			$('#image1').html("<img  src="+x+"  border=3 height=450px width=420px></img>")
			$('#image2').html("<img  src="+y+"  border=3 height=450px width=420px></img>")
		    $('#title1').html(data[0].fields.title);
		    $('#title2').html(data[1].fields.title);
		    $('#like').attr("fashionistaId",data[0].pk);
		    $('#like').attr("userId",data[0].fields.user);
		    $('#like2').attr("fashionistaId",data[1].pk);
		    $('#like2').attr("userId",data[1].fields.user);
		    $('#like_count').html(data[0].fields.likes)
		    $('#like_count2').html(data[1].fields.likes)
		}
		else
		{
			$('#fashionpoll').html("<h2>There are not enough competitiors remaining for competetion!</h2>")
		}
	});
});
$('#like2').click(function(){
	var pid, liked, unliked,x,y;
	pid = $(this).attr("fashionistaId");
	liked = $(this).attr("userId");
	unliked = $('#like').attr("userId");
	$.get('/FashionPoll/like-picture/', { pic_id1 : pid, liked : liked, unliked : unliked }, function(data){
		if(!data.hasOwnProperty('available'))
		{
			x = "http://127.0.0.1:8000/media/"+data[0].fields.fashionista_picture;
			y = "http://127.0.0.1:8000/media/"+data[1].fields.fashionista_picture;
			$('#name1').html(data[0].fields.user);
			$('#name2').html(data[1].fields.user);
			$('#image1').html("<img  src="+x+"  border=3 height=450px width=420px></img>")
			$('#image2').html("<img  src="+y+"  border=3 height=450px width=420px></img>")
		    $('#title1').html(data[0].fields.title);
		    $('#title2').html(data[1].fields.title);
		    $('#like').attr("fashionistaId",data[0].pk);
		    $('#like').attr("userId",data[0].fields.user);
		    $('#like2').attr("fashionistaId",data[1].pk);
		    $('#like2').attr("userId",data[1].fields.user);
		    $('#like_count').html(data[0].fields.likes)
		    $('#like_count2').html(data[1].fields.likes)
		}
		else
		{
			$('#fashionpoll').html("<h2>There are not enough competitiors remaining for competetion!</h2>")
		}
	});
});
});
