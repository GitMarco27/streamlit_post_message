(function() {
    function handleMessage(event) {
        if (event.data.message === window.parent.messageKey) {
            console.log("Receiving a new event: ", event);
            const receivedMessage = JSON.stringify(event.data);
            if (isJsonString(receivedMessage)) {
                const externalMessage = JSON.parse(receivedMessage);

                window.parent.externalMessage = externalMessage;
                console.log("message received: ", externalMessage);

                window.parent.removeEventListener('message', handleMessage);
                console.log("Removing handleMessage EventListener")

            } else {
                console.log("Received message is not a valid JSON string:", receivedMessage);
            }
        }
    }

    function isJsonString(str) {
        try {
            JSON.parse(str);
        } catch (e) {
            return false;
        }
        return true;
    }

    window.parent.addEventListener('message', handleMessage);
    console.log("Event listener added");

    window.parent.parent.postMessage('acknowledgment', '*');
    console.log("Ack sent to the parent window");
})();
