# OOXML snippet library — Thai runs (szCs fix)

Copy these verbatim. Replace `>TEXT<` with your content, XML-escape `&` `<` `>`.
All include BOTH `<w:sz>` and `<w:szCs>` and OMIT `<w:cs/>` — required so Thai glyphs size correctly.

Insert into a **content-scoped range** only:
- Body paragraph: `thPara.getRange("Content").insertOoxml(pkg, "Replace")`
- Table cell: `cell.body.search(thaiText).getFirst().insertOoxml(pkg, "Replace")`

## TH body / list (Angsana New 14pt → sz/szCs 28, blue)
```xml
<?xml version="1.0" standalone="yes"?>
<pkg:package xmlns:pkg="http://schemas.microsoft.com/office/2006/xmlPackage"><pkg:part pkg:name="/_rels/.rels" pkg:contentType="application/vnd.openxmlformats-package.relationships+xml"><pkg:xmlData><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships></pkg:xmlData></pkg:part><pkg:part pkg:name="/word/document.xml" pkg:contentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"><pkg:xmlData><w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:p><w:r><w:rPr><w:rFonts w:ascii="Angsana New" w:hAnsi="Angsana New" w:cs="Angsana New"/><w:color w:val="0000FF"/><w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr><w:t xml:space="preserve">TEXT</w:t></w:r></w:p></w:body></w:document></pkg:xmlData></pkg:part></pkg:package>
```

## TH H2 sibling (Angsana New ~18pt → sz/szCs 36, blue, bold)
```xml
<?xml version="1.0" standalone="yes"?>
<pkg:package xmlns:pkg="http://schemas.microsoft.com/office/2006/xmlPackage"><pkg:part pkg:name="/_rels/.rels" pkg:contentType="application/vnd.openxmlformats-package.relationships+xml"><pkg:xmlData><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships></pkg:xmlData></pkg:part><pkg:part pkg:name="/word/document.xml" pkg:contentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"><pkg:xmlData><w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:p><w:r><w:rPr><w:rFonts w:ascii="Angsana New" w:hAnsi="Angsana New" w:cs="Angsana New"/><w:b/><w:color w:val="0000FF"/><w:sz w:val="36"/><w:szCs w:val="36"/></w:rPr><w:t xml:space="preserve">TEXT</w:t></w:r></w:p></w:body></w:document></pkg:xmlData></pkg:part></pkg:package>
```

## TH safety callout (Angsana New 14pt, blue, shaded #FFF2CC)
```xml
<?xml version="1.0" standalone="yes"?>
<pkg:package xmlns:pkg="http://schemas.microsoft.com/office/2006/xmlPackage"><pkg:part pkg:name="/_rels/.rels" pkg:contentType="application/vnd.openxmlformats-package.relationships+xml"><pkg:xmlData><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships></pkg:xmlData></pkg:part><pkg:part pkg:name="/word/document.xml" pkg:contentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"><pkg:xmlData><w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:p><w:pPr><w:shd w:val="clear" w:color="auto" w:fill="FFF2CC"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Angsana New" w:hAnsi="Angsana New" w:cs="Angsana New"/><w:color w:val="0000FF"/><w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr><w:t xml:space="preserve">TEXT</w:t></w:r></w:p></w:body></w:document></pkg:xmlData></pkg:part></pkg:package>
```

## Verify each run after insert
```js
const xml = thPara.getOoxml(); await ctx.sync();
const ok = /w:szCs/.test(xml.value) && !/<w:cs\/>/.test(xml.value);
```
