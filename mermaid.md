%%Mermaid flowchart editor in VS code <br/>
%%First example
:::mermaid
graph TD
A[Parent procedure]--> B1[Process]
A --> B2[Process]
B1 --> C1[Subprocess]
B2 --> C2[Subprocess]
C1--> D1_1{Decision <br/>to be made}
C1--> D1_2{Primary <br/>concepts}
C1--> D1_3{Alternate}
C2--> D2_1{Decision <br/>to be made}
C2--> D2_2{Primary <br/>concepts}
C2--> D2_3{Alternate}
:::
%%Second example, same nodes
:::mermaid
graph LR
A[Parent procedure]:::pinkClass --> B1[Process]
A --> B2[Process]
subgraph subprocess1
C1[subprocess]--> D1_1{Decision <br/>to be made}
C1--> D1_2{Primary <br/>concepts}
C1--> D1_3{Alternate}
end
subgraph subprocess2
C2[subprocess]--> D2_1{Decision <br/>to be made}:::diamondClass
C2--> D2_2{Primary <br/>concepts}
C2--> D2_3{Alternate}
end
B1-->C1
B2-->C2
style C1 fill:#f9f,stroke:#333,stroke-width:10px
classDef pinkClass fill:#f99;
classDef diamondClass fill:#f10, stroke-width:5px, stroke:#f99;
:::
%% Useful links
https://mermaid-js.github.io/mermaid/overview/n00b-overview.html  <br/>
https://code.visualstudio.com/   <br/>
https://mermaid-js.github.io/mermaid/overview/integrations.html  <br/>
http://shorturl.at/deDEM  <br/>
https://mermaid-js.github.io/mermaid/diagrams-and-syntax-and-examples/flowchart.html <br/>
%%