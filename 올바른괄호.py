function solution(s){
    var answer = true;
    let a=0;
    
   
    
   for(let i =0; i<s.length; i++)
       {
           if(s[i] == "("){
               a+=1;
           }
           else if(s[i] ==")"){
               a -=1;
           }
           if (a<0){
               answer=false;
           }
       }
    
    
    if (a!= 0){
        answer=false;
    }
    
    
    

    return answer;
}