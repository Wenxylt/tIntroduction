    function addField(element) {
        parent = element.parentNode;

        nodePair = document.createElement('div');
        nodePair.setAttribute('class', 'pair');
        nodeKey = document.createElement('input');
        nodeKey.setAttribute('type', 'text');
        nodeKey.setAttribute('class', 'key');
        nodeKey.setAttribute('placeholder', '字段');
        nodeKey.setAttribute('name', parent.childElementCount*2);
        nodeValue = document.createElement('input');
        nodeValue.setAttribute('type', 'text');
        nodeValue.setAttribute('class', 'value');
        nodeValue.setAttribute('placeholder', '值');
        nodeValue.setAttribute('name', parent.childElementCount*2+1);
        nodeDelete = document.createElement('button');
        nodeDelete.setAttribute('class', 'delete');
        nodeDelete.setAttribute('type', 'button');
        nodeDelete.setAttribute('onclick', 'deleteField(this); return false;');
        nodeImage = document.createElement('img');
        nodeImage.setAttribute('src', 'media/minus.svg');
        nodeImage.setAttribute('border', '0');
        nodeDelete.appendChild(nodeImage);
        nodePair.appendChild(nodeKey);
        nodePair.appendChild(nodeValue);
        nodePair.appendChild(nodeDelete);

        parent.insertBefore(nodePair, element);
        return false;
    }

    function deleteField(element) {
        pair = element.parentNode;
        parent = pair.parentNode;
        parent.removeChild(pair);
    }
    function invokeUpload(element) {
        element.parentNode.parentNode.getElementsByClassName('profileupload')[0].click();
    }
