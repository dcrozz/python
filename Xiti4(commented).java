import org.xml.sax.helpers.DefaultHandler;
import org.xml.sax.*;

import javax.xml.parsers.*;

public class Xiti4 {
    public static void main(String[] args) {
        try {
            SAXParserFactory factory = SAXParserFactory.newInstance();//获得解析工厂
            SAXParser saxParser = factory.newSAXParser();//创建解析器
            MyHandler myHandler = new MyHandler();//实例化处理器对象
            saxParser.parse("xiti4.xml", myHandler);//解析指定文件，指定事件处理器
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}

class MyHandler extends DefaultHandler {
    float math = 0, english = 0;
    float m = 0, en = 0;
    int n=0;
    boolean flag = false, fmath = false, feng = false;

    public void startDocument() throws SAXException {
        System.out.print("=====³É¼¨µ¥=====");
    }

    public void endDocument() throws SAXException {
        System.out.println("=====Æ½¾ù·Ö=====");
        System.out.println("ÊýÑ§£º"+(math/n));
        System.out.println("Ó¢Óï£º"+(english/n));
    }

    public void startElement(String uri, String localName, String qName, Attributes attributes) throws SAXException {
        if (qName.equals("name")) {
            flag = true;
            n++;
        }
        if (qName.equals("math")) {
            fmath = true;
        }
        if (qName.equals("english")) {
            feng = true;
        }
    }

    public void endElement(String uri, String localName, String qName) throws SAXException {
        if (qName.equals("name")) {
            System.out.println("×Ü·Ö:" + (m + en));
        }
    }

    public void characters(char ch[], int start, int length) throws SAXException {
        if (flag) {
            System.out.println(new String(ch, start, length));
            flag = false;
        }
        if (fmath) {
            m = Float.parseFloat(new String(ch, start, length));
            System.out.println("ÊýÑ§£º" + m);
            math += m;
            fmath = false;
        }
        if (feng) {
            en = Float.parseFloat(new String(ch, start, length));
            System.out.println("Ó¢Óï£º" + en);
            english += en;
            feng = false;
        }
    }
}



