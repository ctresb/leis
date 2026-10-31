// Uso: node renderizar_markdown_reparo.mjs /caminho/marked/lib/marked.esm.js
import {pathToFileURL} from 'node:url';
const {marked} = await import(pathToFileURL(process.argv[2]).href);
process.stdin.setEncoding('utf8');
let source = '';
for await (const chunk of process.stdin) source += chunk;
process.stdout.write(marked.parse(source));
