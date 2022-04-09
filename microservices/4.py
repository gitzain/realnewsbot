# Summarises the text given to it

import json
from flask import request

#Import library essentials
from sumy.parsers.plaintext import PlaintextParser #We're choosing a plaintext parser here, other parsers available for HTML etc.
from sumy.nlp.tokenizers import Tokenizer 
from sumy.summarizers.lex_rank import LexRankSummarizer #We're choosing Lexrank, other algorithms are also built in
from flask import Flask
from flask_restplus import Resource, Api, fields, Namespace

app = Flask(__name__)

app.config.SWAGGER_UI_DOC_EXPANSION = 'list'
api = Api(app, 
          version='1.0',
          title='Summary API', 
          description='This API summarises text given to it.',
          default='summary',
          default_label='summarises text')

class Summary:
    def summarise(self, text):
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LexRankSummarizer()
        summary = summarizer(parser.document, 5) #Summarize the document with 5 sentences

        result = ""
        for sentence in summary:
            result += " " + str(sentence)

        return result

###########################################################

@api.route('/summarise')
class SummaryAPI(Resource):
    text = api.model('Text', {
    'text': fields.String
    })

    @api.expect(text)
    #@api.marshal_with(text, code=200)
    def post(self):
        print "INPUT **************************"
        print request.json
        result = Summary().summarise(request.json['text'])
        data = {}
        data['text'] = result
        print "OUTPUT **************************"
        res= json.dumps(data)
        print res
        return res

###########################################################

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)
