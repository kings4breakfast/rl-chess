import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;

public class Dummy {
    public static void main(String[] args) throws IOException {
        // Reset the environment
        sendPost("http://localhost:5000/reset", "{}");

        // Example move: from [1,0] to [2,0]
        String moveJson = "{\"action\": [[1, 0], [2, 0]]}";
        String response = sendPost("http://localhost:5000/step", moveJson);

        System.out.println("Response from Python chess env:");
        System.out.println(response);
    }

    public static String sendPost(String targetURL, String jsonInputString) throws IOException {
        URL url = new URL(targetURL);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();

        conn.setRequestMethod("POST");
        conn.setRequestProperty("Content-Type", "application/json; utf-8");
        conn.setDoOutput(true);

        try (OutputStream os = conn.getOutputStream()) {
            byte[] input = jsonInputString.getBytes("utf-8");
            os.write(input, 0, input.length);
        }

        BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream(), "utf-8"));
        StringBuilder response = new StringBuilder();
        String responseLine;

        while ((responseLine = br.readLine()) != null) {
            response.append(responseLine.trim());
        }

        return response.toString();
    }
}
