/**
 * Created by JH on 2017-03-05.
 */

function loadCombo(target, data) {   // clear existing items in combo, and add new items to the target object
    //alert(data);
    var dataArr = [];
    var inx = 0;
    target.empty();
    // console.log("load combo");
    // if (target.name == 'gu_code') {
    //     dataArr[inx++] = "<option value=0>구/군 선택</option> ";
    // } else if(target.name=='dong_code'){
    //     dataArr[inx++] = "<option value=0>동 선택</option> ";
    // }

    $(data).each(function () {
        dataArr[inx++] = "<option value=" + this.code + ">" + this.name + "</option> ";
    });


    target.append(dataArr);

}

function current_year(){
    var d = new Date();
    return d.getFullYear();
}

function current_quarter(){
    var d = new Date();
    return (Math.floor((d.getMonth() + 1 ) / 4 )+1);
}


