var shittyArray = [hataData,hataData,hataData,hataData,hataData,hataData,hataData,hataData];

shittyArray.filter(onlyUnique);
console.log(shittyArray);

function onlyUnique(value, index, self) { 
    return self.indexOf(value) === index;
}