// const Sitemapper = require('sitemapper');

// const sitemap = new Sitemapper();

// sitemap.fetch('https://spankbang.com/sitemap/1.xml').then(function(sites) {
//   console.log(sites);
// });  2/3/30/34/35

const SitemapXMLParser = require('sitemap-xml-parser');

const url = 'https://spankbang.com/sitemap/3';

const options = {
    delay: 3000,
    limit: 5
};

const sitemapXMLParser = new SitemapXMLParser(url, options);

sitemapXMLParser.fetch().then(result => {
    let locID = result[0]['loc'][0].split(/\//gm)[3];
    let locName = result[0]['loc'][0].split(/\//gm)[5];
    let locNameTilte = locName.replace(/\+/gm," ");
    let locNameTag = locName.replace(/\+/gm,"','");
    console.log(locID,locNameTilte,locNameTag);
});
