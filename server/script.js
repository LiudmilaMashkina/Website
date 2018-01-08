function scale_tree()
{
    var img = $('#christmas_tree')
    var img_natural_w = img[0].naturalWidth
    var img_natural_h = img[0].naturalHeight
    
    var img_h = $('#christmas_tree_anchor').height() * 1.7
    var img_w = img_h * img_natural_w / img_natural_h
    $('#christmas_tree').width(img_w).height(img_h)
};

function scale_magnifier()
{
    var img = $('#magnifier')
    var img_natural_w = img[0].naturalWidth
    var img_natural_h = img[0].naturalHeight
    
    var img_h = $('#magnifier_anchor').height() * 0.9
    var img_w = img_h * img_natural_w / img_natural_h
    $('#magnifier').width(img_w).height(img_h)
}

function scale_main_pic()
{
    var img = $('#main_pic')
    var img_natural_w = img[0].naturalWidth
    var img_natural_h = img[0].naturalHeight
    
    var img_h = $('#main_pic_anchor').height()
    var img_w = img_h * img_natural_w / img_natural_h

    var total_w = $('#main_pic_system').width()

    var wrap_h = img_h
    var wrap_w = total_w

    $('#main_pic').width(img_w).height(img_h)
    $('#main_pic_wrap').width(wrap_w).height(wrap_h)
    $('#blue').height(img_h)
}

function scale() {
    scale_tree()
    scale_magnifier()
    scale_main_pic()
}

$(window).on("load", function() {
    scale()
})

$(window).resize(function(){
    scale()
});
