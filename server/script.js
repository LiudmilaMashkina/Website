function scale_tree()
{
    var img = $('#christmas_tree')
    var img_natural_w = img[0].naturalWidth
    var img_natural_h = img[0].naturalHeight
    
    var img_h = $('#christmas_tree_anchor').height() * 1.7
    var img_w = img_h * img_natural_w / img_natural_h
    $('#christmas_tree').width(img_w).height(img_h)
};

$(window).on("load", function() {
    scale_tree()
})
