#!/usr/bin/node
const historyKingsData = [
    {
      "ethiopianKings": [
        "ልብነ ድንግል", "ገላውዴዎስ", "ሚናስ", "ሰርፀድንግል", "ሚናስ ", "  ያዕቆብ", "ዘድንግል",
        " ሱስንዮስ", "ፋስል", "ዮሐንስ ", "አድያም ሰገድ ኢያሱ", "ረጉም ተክለሀይማኖት",
        " ቴዎፍሎስ ", "ዮስጦስ ", " ዳዊት", " በካፋ ", " ቋረኛው ኢያሱ", "ኢዮአስ ",
        " አንድ እጅ ዮሀንስ", "ተክለ ለሀይማኖት ", "ተክለጊዮርጊስ ", " አፄ ቴዎድሮስ | የቋራው ካሳ ",
        " ዋግሹም ጎበዜ", " አፄ ዮሀንስ | ዮሀንስ | አጤ ዮሀንስ ", "አጤ ምኒሊክ| አፄ | ምኒሊክ  ",
        " ሀይለ ስላሴ", " ", "  "
      ]
    }
  ];
  
  // Function to search for a king's name using regex
  function findKing(name) {
    const regex = new RegExp(name.trim(), "i"); // "i" makes it case-insensitive
    return historyKingsData[0].ethiopianKings.filter(king => regex.test(king.trim()));
  }
  
  // Example: Searching for "ዮሀንስ"
  const searchResult = findKing("አጤ ዮሀንስ");
  console.log(searchResult[0]); // ["ዮሀንስ ", " አፄ ዮሀንስ | ዮሀንስ | አጤ ዮሀንስ "]
  