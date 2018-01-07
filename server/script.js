function scale_tree()
{
    $img = $('#christmas_tree')
    $img_natural_w = $img[0].naturalWidth
    $img_natural_h = $img[0].naturalHeight
    
    $img_h = $('#christmas_tree_anchor').height() * 1.7
    $img_w = $img_h * $img_natural_w / $img_natural_h
    $('#christmas_tree').width($img_w).height($img_h)
};

$(window).on("load", function() {
    scale_tree()
})
