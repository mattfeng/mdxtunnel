# mdxtunnel

_Proxies requests for MDX content to the appropriate (filesystem) source._

`mdxtunnel` is needed to separate the sending of MDX content to `quetzalcoatl`
from the actual content itself, which allows multiple different sites to only
need to alter their content.
