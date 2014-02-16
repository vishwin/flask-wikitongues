$(function(){

	$('#nav-button').on('click', function(){
	    $('#wrapper, #tubular-container, #tubular-shield, .metadata').toggleClass('left-animate')
	})

	$('#submit-form').on('click', function(){
	    $('#form-wrapper').show()
	})

	$('#close-button').on('click', function(e){
	        $('#form-wrapper').hide();
	});

	$('body').on('keydown', function(e){
	    if ((e.keyCode || e.which) == 27)
	    {
	        $('#form-wrapper').hide();
	    }  
	});

	$('.select select').each(function(){
	  $(this).change(function() {
	    var str = "";
	    $(this).find("option:selected").each(function(){
	      str += $(this).text() + " ";
	    });
	    $(this).siblings('span').text(str);
	  }).change(); 

	});

	$('.upload input').change(function(){
	    var fileValue = $('.upload input').attr('value')
	    $(this).siblings('span').text(fileValue)
	});

	var link_click_handler = function(event) {
	    event.preventDefault();

	    var the_link = $(this);

	    activate_section(the_link);
	};

	var activate_section = function(the_link) {
	    the_link.attr('style','background:#A8A9AA;');

	    var other_links = the_link.parent().siblings().find('button').removeAttr('style'); 

	    var href = the_link.attr('data-section'); 

	    console.log(href)

	    var corresponding_section = $(href);
	    corresponding_section.show();

	    var other_sections = corresponding_section.siblings();
	    other_sections.hide();
	};


	$(function() {

	    var link_selector = $('ul#filter li button');
	    var links = $(link_selector);

	    links.on('click', link_click_handler);

	    var first_link = links.eq(0);

	    activate_section(first_link);
	});

	$('.cat-list li').on('click', function(){
	    $(this).find('.sub-nav').toggle()
	});

	});

})
