import unittest
import scipy
from nltk.classify import ClassifierI
import YesMan
import win32gui

class KnownValues(unittest.TestCase):
    def testMode1(self):
        votes = [1, 1, 1, 1, 1, 1, 1]
        clas = scipy.stats.mstats.mode(votes)
        self.assertEqual(clas.mode, 1)


    def testMode0(self):
        votes = [0, 0, 0, 0, 1, 1, 1]
        clas = scipy.stats.mstats.mode(votes)
        self.assertEqual(clas.mode, 0)

    def testPos(self):
        PosEULAfromTrainingfeats={'limited': True, 'results': True, 'facilities': True, 'gb': True, 'llc': True, 'follow': True, 'causes': True,
         'whose': True, 'granting': True, '0': True, 'hereof': True, 'permanently': True, 'teaching': True,
         'activities': True, 'belonging': True, 'downloading': True, 'returned': True, 'sitting': True,
         'infringement': True, 'void': True, 'choice': True, 'liability': True, 'updates': True, 'advised': True,
         'entire': True, 'accompanying': True, 'forth': True, 'rights': True, 'list': True, 'applicable': True,
         'biological': True, 'disclaimer': True, 'specially': True, 'construed': True, 'direct': True, 'licensed': True,
         '95054': True, 'licenses': True, 'cfr': True, 'machines': True, 'even': True, 'section': True,
         'foregoing': True, 'version': True, 'new': True, 'apply': True, 'deemed': True, 'full': True, 'iran': True,
         'degree': True, 'owns': True, 'modify': True, 'disclaim': True, 'downloaded': True, 'possibility': True,
         'others': True, 'decipher': True, 'iraq': True, 'table': True, 'obtained': True, 'thirty': True,
         'expressly': True, 'employees': True, '30': True, 'trial': True, 'products': True, 'action': True,
         'changes': True, 'control': True, 'requiring': True, 'clara': True, 'licensing': True, 'reserved': True,
         'total': True, 'use': True, '6': True, 'survive': True, 'exported': True, 'injury': True, 'type': True,
         'authorization': True, 'initiated': True, 'hereby': True, 'validity': True, 'purposes': True,
         'particular': True, 'known': True, 'behalf': True, 'must': True, 'high': True, 'none': True, 'f': True,
         'challenge': True, 'installing': True, 'remain': True, 'anywhere': True, 'install': True, 'following': True,
         'meet': True, 'example': True, 'purchaser': True, 'workstations': True, 'share': True, 'updated': True,
         'states': True, 'minimum': True, 'purchased': True, 'interpreted': True, 'exclude': True, 'risk': True,
         'information': True, 'educational': True, 'united': True, 'end': True, 'provide': True, 'country': True,
         'indirectly': True, 'damage': True, '1': True, 'located': True, 'product': True, 'express': True,
         'description': True, 'disassemble': True, 'specifications': True, 'abuse': True, 'designed': True,
         'nonexclusive': True, 'date': True, 'representations': True, 'law': True, 'data': True, 'types': True,
         'purchase': True, 'workstation': True, 'attempt': True, 'effective': True, 'documentation': True,
         'destroying': True, 'allow': True, 'granted': True, 'refund': True, 'restriction': True, 'feedback': True,
         'misapplication': True, 'institutional': True, 'consent': True, 'reserves': True, 'entity': True,
         'statutory': True, 'including': True, 'chemical': True, 'negotiated': True, '20': True, 'exclusion': True,
         'acknowledge': True, 'personal': True, 'exclusions': True, 'actually': True, 'tort': True, 'production': True,
         'systems': True, 'constitutes': True, 'consequential': True, 'subparagraph': True, 'alter': True, 'non': True,
         'return': True, 'outlined': True, 'safe': True, 'cpus': True, 'warranted': True, 'provision': True,
         'instructions': True, 'term': True, 'commands': True, 'fitness': True, 'found': True, 'nationals': True,
         'defects': True, 'prohibit': True, 'receipt': True, 'principles': True, 'related': True,
         'cryptosidekick': True, 'punitive': True, 'instrumentalities': True, 'substantially': True, 'operation': True,
         'event': True, 'special': True, 'intended': True, 'network': True, 'profit': True, 'restricted': True,
         'enforceable': True, 'research': True, 'may': True, 'evaluation': True, 'state': True, 'syria': True,
         'free': True, 'california': True, 'conflicts': True, 'remainder': True, 'definition': True, 'training': True,
         'licensors': True, 'workmanship': True, 'g': True, 'could': True, 'days': True, 'subparagraphs': True,
         'tolerant': True, 'place': True, 'incorporated': True, 'retain': True, 'assign': True, 'purpose': True,
         'features': True, 'revenue': True, 'clause': True, 'number': True, 'thereof': True, 'one': True,
         'instances': True, 'specifically': True, 'directly': True, 'fees': True, 'quality': True, 'engineer': True,
         'service': True, 'introduction': True, 'twenty': True, 'anyone': True, '2': True, 'listed': True,
         'convention': True, 'lease': True, 'option': True, 'releases': True, 'acquire': True, 'lists': True,
         'environmental': True, 'part': True, 'copy': True, 'representing': True, 'kind': True, 'b': True,
         'accordance': True, '19': True, 'nations': True, 'matter': True, 'protected': True, 'gives': True,
         'solely': True, 'result': True, 'function': True, 'correction': True, 'manner': True, 'null': True,
         'orders': True, 'also': True, 'internal': True, 'transmit': True, 'destroy': True, 'regard': True,
         'unless': True, 'shall': True, 'price': True, 'expires': True, 'paid': True, 'scripts': True, 'services': True,
         'america': True, 'deny': True, 'released': True, 'sale': True, 'order': True, 'professional': True,
         'duplication': True, 'laws': True, 'exclusive': True, 'violation': True, 'jurisdiction': True,
         'terminate': True, 'determined': True, 'availability': True, 'upgrade': True, 'copyright': True, 'title': True,
         'merger': True, 'written': True, 'employer': True, 'failed': True, 'explicitly': True, 'treasury': True,
         'cuba': True, '52': True, 'means': True, 'vary': True, 'de': True, 'designated': True, 'incidental': True,
         'remedy': True, 'international': True, 'installed': True, 'reinstall': True, 'comply': True, 'countries': True,
         'h': True, 'remove': True, 'whether': True, '2142': True, 'liable': True, 'release': True, 'set': True,
         'acquired': True, 'national': True, 'computer': True, 'descriptions': True, 'fail': True, 'subject': True,
         'fails': True, 'binds': True, 'federal': True, 'nuclear': True, 'representatives': True, 'materials': True,
         'weapons': True, '3': True, 'future': True, 'neither': True, 'conditions': True, 'supersedes': True,
         'available': True, 'notice': True, 'korea': True, 'terms': True, 'commercial': True, 'sold': True,
         'sole': True, 'however': True, 'agencies': True, 'aircraft': True, 'extent': True, 'restrictions': True,
         'c': True, 'accident': True, 'installation': True, 'reverse': True, 'license': True, 'fault': True,
         'quiet': True, 'contract': True, 'assure': True, 'connection': True, 'otherwise': True, 'exemplary': True,
         'ca': True, 'period': True, 'environments': True, 'grants': True, 'agents': True, 'contemporaneous': True,
         '252': True, 'respect': True, 'described': True, 'basis': True, 'trademark': True, 'copies': True,
         'mark': True, 'agreements': True, 'interest': True, 'life': True, 'received': True, 'dates': True,
         'understand': True, 'prices': True, 'case': True, 'commerce': True, 'libya': True, 'air': True,
         'compile': True, 'technical': True, 'expiration': True, 'error': True, 'property': True, 'rent': True,
         'concurrently': True, 'resident': True, 'characteristics': True, 'herein': True, 'according': True, 'ii': True,
         'kingsbury': True, 'technology': True, 'grant': True, 'perform': True, 'media': True, 'make': True,
         'cumulative': True, 'damages': True, 'copying': True, 'modification': True, 'party': True, 'development': True,
         'used': True, 'temporary': True, 'enjoyment': True, 'assignment': True, 'upon': True, 'effect': True,
         'persons': True, 'running': True, 'user': True, 'ownership': True, 'opportunity': True, 'programs': True,
         'navigation': True, 'academic': True, 'severe': True, 'without': True, 'termination': True, 'arising': True,
         'obtain': True, 'underlying': True, 'using': True, 'electronically': True, 'death': True, 'equipment': True,
         'except': True, 'capabilities': True, 'governmental': True, 'copyrights': True, '4': True, 'provisions': True,
         'government': True, 'read': True, 'evaluate': True, 'discontinue': True, 'whichever': True, 'royalty': True,
         'traffic': True, 'performance': True, 'world': True, 'accepted': True, 'loss': True, 'modifications': True,
         'like': True, 'suppliers': True, 'perpetual': True, 'server': True, 'specific': True, 'communications': True,
         'either': True, 'fully': True, 'prior': True, 'essential': True, 'replacement': True, 'exceed': True,
         'right': True, 'unenforceable': True, 'export': True, 'specified': True, 'duration': True, 'indirect': True,
         'dfars': True, 'warranting': True, 'provided': True, 'lead': True, 'sudan': True, 'lend': True,
         'integration': True, 'legal': True, 'provides': True, 'understandings': True, 'warranties': True,
         'limitations': True, 'knew': True, 'business': True, 'manufactured': True, 'agreement': True,
         'prohibited': True, 'santa': True, 'relating': True, 'permitted': True, 'nontransferable': True,
         'limitation': True, 'goods': True, 'efforts': True, 'software': True, 'warranty': True, 'repair': True,
         'interruption': True, 'communication': True, 'warrants': True, 'within': True, 'bound': True,
         'intellectual': True, 'servers': True, 'parties': True, '7013': True, '1980': True, 'transfer': True,
         'support': True, 'long': True, 'authorized': True, 'translate': True, 'sections': True, 'files': True,
         'north': True, 'hazardous': True, 'criteria': True, 'failure': True, 'properly': True, 'courts': True,
         'scope': True, '227': True, 'e': True, 'line': True, 'made': True, 'licensees': True, 'maximum': True,
         'signed': True, 'cir': True, 'sublicense': True, 'agree': True, 'delete': True, 'associated': True,
         'defined': True, 'general': True, 'single': True, 'governed': True, 'file': True, 'ship': True,
         'physical': True, 'functions': True, 'us': True, '48': True, 'contest': True, 'agreeing': True,
         'application': True, 'valid': True, '5': True, 'department': True, 'unwilling': True, 'users': True,
         'separate': True, 'update': True, 'regulations': True, 'concurrent': True, 'merchantability': True,
         'disclosure': True, 'hereunder': True, 'individual': True, 'longer': True, 'assume': True, 'required': True,
         'together': True, 'original': True, 'resale': True, 'implied': True, 'u': True, 'time': True, 'oral': True,
         'receive': True}
        vote=YesMan.voted_classifier.classify(PosEULAfromTrainingfeats)
        self.assertEqual(vote, "neg")

    def tesNeg(self):
        NegEULAfromTrainingfeats={'minors': True, 'caused': True, 'existing': True, 'supplement': True, 'hereto': True, 'children': True,
         'hunting': True, 'list': True, 'finally': True, 'hereof': True, 'permanently': True, 'breach': True,
         'include': True, 'fences': True, 'cruising': True, 'terminate': True, 'void': True, 'liability': True,
         'every': True, 'minerals': True, 'condition': True, 'governments': True, 'entire': True, 'cause': True,
         'rights': True, 'companies': True, 'applicable': True, 'leave': True, 'indemnity': True, 'noted': True,
         'prevent': True, 'charter': True, 'force': True, 'occurrence': True, 'fence': True, 'construed': True,
         'direct': True, 'sign': True, 'notwithstanding': True, 'giving': True, 'public': True, 'deemed': True,
         'full': True, 'guardian': True, 'understanding': True, 'operating': True, 'others': True, 'sublease': True,
         'change': True, 'obtained': True, 'silvicultural': True, 'thirty': True, 'expressly': True, 'employees': True,
         'compliance': True, 'prior': True, 'amount': True, 'products': True, 'therein': True, 'cancellation': True,
         'named': True, 'regardless': True, 'secure': True, 'private': True, 'county': True, 'egress': True,
         'names': True, 'firearm': True, 'use': True, 'contains': True, 'athens': True, 'overhead': True, '6': True,
         'agreeable': True, 'injury': True, 'posting': True, 'started': True, 'becomes': True, 'aware': True,
         'hold': True, 'effort': True, 'behalf': True, 'shoot': True, 'none': True, 'f': True, 'work': True,
         'modified': True, 'remain': True, 'paragraph': True, 'following': True, 'making': True, 'reserved': True,
         'give': True, 'purposes': True, 'states': True, 'reserves': True, 'allowed': True, 'hereinafter': True,
         'occur': True, 'information': True, 'united': True, 'end': True, 'provide': True, 'acts': True, 'damage': True,
         '1': True, 'located': True, 'forest': True, 'gate': True, 'invitees': True, 'commencing': True, 'may': True,
         'designated': True, 'membership': True, 'abuse': True, 'trees': True, 'date': True, 'representations': True,
         'derives': True, 'effective': True, 'supervision': True, 'maintain': True, 'responsibility': True,
         'deposit': True, 'allow': True, 'enter': True, 'rentals': True, 'first': True, 'granted': True,
         'exclusive': True, 'ingress': True, 'rifles': True, 'lands': True, 'including': True, 'easements': True,
         'accepted': True, 'lessor': True, 'personal': True, 'heretofore': True, 'vicinity': True, 'acres': True,
         'harmless': True, 'policy': True, 'therefor': True, 'damages': True, 'good': True, 'material': True,
         'hunter': True, 'cutting': True, 'party': True, 'provision': True, 'day': True, 'association': True,
         'term': True, 'name': True, 'fully': True, 'reasonably': True, 'reasonable': True, 'found': True,
         'referred': True, 'house': True, 'constitute': True, 'fires': True, 'oil': True, 'year': True, 'event': True,
         'witness': True, 'sustains': True, 'termination': True, 'defend': True, 'safety': True, '7': True,
         'forth': True, 'thereupon': True, 'written': True, 'put': True, 'obligation': True, 'retained': True,
         'g': True, 'days': True, 'produce': True, 'incorporated': True, 'regress': True, 'onto': True, 'assign': True,
         'designed': True, 'thereon': True, 'clause': True, 'thereof': True, 'one': True, 'feet': True,
         'improvements': True, 'notify': True, 'directly': True, 'open': True, 'covenants': True, 'law': True,
         'least': True, 'anyone': True, '2': True, 'farming': True, 'structures': True, 'lease': True, 'option': True,
         'part': True, 'suitability': True, 'copy': True, '11': True, '10': True, '13': True, 'b': True, '15': True,
         '14': True, '17': True, '16': True, '19': True, '18': True, 'submitted': True, 'preparation': True,
         'compensation': True, 'determined': True, 'contrary': True, 'risks': True, 'solely': True, 'partnership': True,
         'thereto': True, 'rent': True, 'recover': True, 'responsible': True, 'officers': True, 'practices': True,
         'trespassing': True, 'build': True, 'barn': True, 'shall': True, 'indemnification': True, 'paid': True,
         'tract': True, 'payment': True, 'acknowledges': True, 'insured': True, 'laws': True, 'violation': True,
         'agreed': True, 'affix': True, 'pursuant': True, 'ending': True, 'trespass': True, 'executed': True,
         'defects': True, 'agrees': True, 'ground': True, 'removed': True, 'latent': True, 'title': True,
         'merger': True, 'state': True, '8': True, 'local': True, 'merged': True, 'prosecute': True, 'permission': True,
         'contracts': True, 'leased': True, 'kind': True, 'bear': True, '12': True, 'occupant': True, 'leases': True,
         'comply': True, 'areas': True, 'regarding': True, 'addresses': True, 'whether': True, 'liable': True,
         'ohio': True, 'implication': True, 'precaution': True, 'set': True, 'reference': True, 'shareholders': True,
         'accord': True, 'individual': True, 'result': True, 'close': True, 'subject': True, 'said': True,
         'clearing': True, '3': True, 'closed': True, 'affecting': True, 'boundary': True, 'vices': True,
         'conditions': True, 'across': True, 'available': True, 'notice': True, 'terms': True, 'nature': True,
         'premises': True, 'however': True, 'interfere': True, 'cut': True, 'premise': True, 'approval': True,
         'c': True, 'taking': True, 'according': True, 'designees': True, 'etc': True, 'connection': True,
         'unincorporated': True, 'otherwise': True, 'extent': True, 'hereunto': True, 'whereof': True, 'agents': True,
         'cancel': True, 'writing': True, 'grazing': True, 'described': True, 'addition': True, 'damp': True,
         'erect': True, 'agreements': True, 'entitle': True, 'acre': True, 'privilege': True, 'entered': True,
         'direction': True, 'controlled': True, 'fire': True, 'gas': True, 'protect': True, 'present': True,
         'lessee': True, 'amend': True, 'expiration': True, 'property': True, 'changed': True, 'unearned': True,
         'herein': True, 'expenses': True, 'damaged': True, 'patent': True, 'pay': True, 'make': True, 'wherein': True,
         'firearms': True, '9': True, 'resulting': True, 'entitled': True, 'used': True, 'assigns': True,
         'assignment': True, 'upon': True, 'effect': True, '000': True, 'purpose': True, 'contractors': True,
         'kept': True, 'haul': True, 'mortgages': True, 'person': True, 'without': True, 'claims': True,
         'arising': True, 'prevention': True, 'agency': True, 'less': True, 'protecting': True, 'injuries': True,
         'timber': True, 'death': True, 'except': True, 'parents': True, '4': True, 'wet': True, 'amended': True,
         'rules': True, 'game': True, '30': True, 'immediately': True, 'execution': True, 'hereafter': True,
         'loss': True, 'necessary': True, 'hunt': True, 'payments': True, 'become': True, 'amendment': True,
         'right': True, 'landowner': True, 'understood': True, 'encumbrances': True, 'escape': True, 'provided': True,
         'connecting': True, 'refundable': True, 'propagating': True, 'warranties': True, 'post': True, 'burn': True,
         'agreement': True, 'relating': True, 'permitted': True, 'conducting': True, 'actual': True, 'anything': True,
         'stand': True, 'road': True, 'warranty': True, 'repair': True, 'referenced': True, 'burning': True,
         'previously': True, 'within': True, 'integral': True, 'lies': True, 'appropriate': True, 'parties': True,
         'roads': True, 'renewal': True, 'removing': True, 'specifically': True, 'way': True, 'assumes': True,
         'therefrom': True, 'maintenance': True, 'vehicle': True, 'payable': True, 'properly': True, 'survive': True,
         'sustained': True, 'surrender': True, 'made': True, 'consist': True, 'licensees': True, 'liens': True,
         'site': True, 'agree': True, '150': True, 'defined': True, 'reservations': True, 'deer': True,
         'shooting': True, 'check': True, 'planting': True, 'marking': True, 'corporation': True, 'insurance': True,
         'forestry': True, 'club': True, 'holding': True, 'nay': True, 'indemnify': True, 'refunded': True,
         'regulations': True, 'land': True, 'e': True, 'assume': True, 'vehicles': True, 'together': True,
         'commencement': True, 'directors': True, 'theretofore': True, 'time': True, 'reserve': True, 'oral': True,
         'indirectly': True}
        vote=YesMan.voted_classifier.classify(NegEULAfromTrainingfeats)
        self.assertEqual(vote, "neg")


    def testTitle(self):
        import win32gui
        Title = (win32gui.GetWindowText(YesMan.hwnd)).lower()
        self.assertEqual("setup" in Title.split() or "license" in Title.split() or "agreement" in Title.split(), "setup"  or "license" or "agreement" )


    def ClientSocketSend(self):
        import Client
        import Server
        Send= Client.ClientSocket.send(Client.EULA)
        Receive = Server.clientsocket.recv(90000)
        self.assertEqual(Send, Receive)

if __name__ == "__main__":
    unittest.main()
