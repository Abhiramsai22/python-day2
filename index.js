function processorder(orderid,callback){
    if(orderid==''){
        callback(false,"order process failed")
    }
    else{
        callback(true,"order process success")
    }
}

function shiporder(orderid,callback){
    if(orderid=="FAIL")
    {
        callback(false,"shipping failed")
    }
    else{
        callback(true,"order shipped with tracking:xyz123")
    }
}

function dispatchorder(orderid,callback){
    if(orderid=="DELAY"){
        callback(false,"dispatch failed")
    }
    else{
        callback(true,"order dispatched with vehcile-1")
    }
}

function outfordelivery(orderid,callback){
    if(orderid=="FAILED"){
        callback(false,"delivery failed")
    }
    else{
        callback(true,"order is out for delivery")
    }
}

processorder("",(status,message)=>{
    if(status==true){
        console.log(message)
        shiporder("FAIL",(status,message)=>{
            if(status==true){
                console.log(message)
                dispatchorder("DELAY",(status,message)=>{
                    if(status==true){
                        console.log(message)
                        outfordelivery("FAILED",(status,message)=>{
                            if(status==true){
                                console.log(message)
                            }
                            else{
                                console.log(message)
                            }
                        })
                    }
                    else{
                        console.log(message)
                    }
                })
            }
            else{
                console.log(message);
            }
        })
    }
    else{
        console.log(message)
    }
})